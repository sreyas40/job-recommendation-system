import httpx
from fastapi import APIRouter, Depends, HTTPException, status, Query, Header
from typing import Type, List, Optional
from .. import (
    get_db,
    Session,
    jobschema,
    jobmodel,
    jobcrud,
    check_authorization,
    get_current_user,
    get_company_details,
)

job_vacancy_router = APIRouter(prefix="/job_vacancy")


@job_vacancy_router.get("/")
async def read_filtered_job_vacancies(
    title: Optional[str] = None,
    emp_type: Optional[List[str]] = Query(None),
    work_style: Optional[List[str]] = Query(None),
    working_days: Optional[List[str]] = Query(None),
    location: Optional[List[str]] = Query(None),
    experience: Optional[List[str]] = Query(None),
    salary: Optional[int] = Query(None),
    skills: Optional[List[str]] = Query(None),
    sort: Optional[str] = None,
    order: Optional[str] = "asc",
    limit: Optional[int] = None,
    db: Session = Depends(get_db),
):
    filter_job_id = None
    if skills is not None:
        filter_job_id = jobcrud.skills.get_filtered_skills(db, skills)
    filtered_jobs = jobcrud.vacancy.get_filtered_jobs(
        db,
        emp_type,
        work_style,
        location,
        working_days,
        salary,
        experience,
        filter_job_id,
        sort,
        order,
        limit,
        title,
    )
    for job in filtered_jobs:
        job.skills = jobcrud.skills.get_all(db, job.job_id)
        # job.company_pic =
        job.job_seekers = jobcrud.request.get_all_by_job_id(db, job.job_id)
    return filtered_jobs


@job_vacancy_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_job_vacancy(
    job_vacancy: jobschema.JobVacancyCreate,
    db: Session = Depends(get_db),
    authorization: str = Header(...),
):
    company_details = await get_company_details(authorization=authorization)
    job_vacancy.company_id = company_details.get("user_id")
    job_vacancy.company_name = company_details.get("company_name")
    job_vacancy.company_username = company_details.get("username")
    data = job_vacancy.dict()
    skill = data.pop("skills", [])

    job_vacancy_instance = jobmodel.JobVacancy(**data)
    if not jobcrud.vacancy.create(db, job_vacancy_instance):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Data not updated to Database",
        )
    job_id = job_vacancy_instance.job_id

    for _ in skill:
        job_skill_data = jobschema.JobSkillsCreate(job_id=job_id, skill=_)
        jobcrud.skills.create(db, job_skill_data)

    job_model = jobschema.JobDetails(**data)
    with httpx.AsyncClient() as client:
        response = await client.post(
            "http://172.20.0.5:8000/job/input",
            json=job_model.dict(),
        )
        if response.status_code != status.HTTP_200_OK:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Error Occured"
            )

    return {"details": "Job Created"}


@job_vacancy_router.get("/model/data")
async def read_job_vacancies_by_company_id(db: Session = Depends(get_db)):
    return jobcrud.vacancy.get_all_for_model(db)


@job_vacancy_router.get("/company")
async def read_job_vacancies_by_company_id(
    db: Session = Depends(get_db), authorization: str = Header(...)
):
    user = await get_current_user(authorization=authorization, user_type="recruiter")
    company_id = user.get("user_id")
    job_vacancy = jobcrud.vacancy.get_all(db, company_id)
    for job in job_vacancy:
        job.skills = jobcrud.skills.get_all(db, job.job_id)
        job.job_seekers = jobcrud.request.get_all_by_job_id(db, job.job_id)
        job.job_invite = jobcrud.invite.get_all_by_job_id(db, job.job_id)
    return job_vacancy


@job_vacancy_router.get("/company/{company_id}")
async def read_job_vacancies_by_company_id(
    company_id: int, db: Session = Depends(get_db)
):

    job_vacancy = jobcrud.vacancy.get_all(db, company_id)
    for job in job_vacancy:
        job.skills = jobcrud.skills.get_all(db, job.job_id)
        job.job_seekers = jobcrud.request.get_all_by_job_id(db, job.job_id)
    return job_vacancy


# Read job vacancy by ID
@job_vacancy_router.get("/{job_vacancy_id}", response_model=jobschema.JobVacancy)
async def read_job_vacancy(job_vacancy_id: int, db: Session = Depends(get_db)):
    db_job_vacancy = jobcrud.vacancy.get(db, job_vacancy_id)
    if db_job_vacancy is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Job Vacancy not found"
        )
    return db_job_vacancy


# Update job vacancy by ID
@job_vacancy_router.put("/{job_vacancy_id}")
async def update_job_vacancy(
    job_vacancy_id: int,
    job_vacancy: jobschema.JobVacancyUpdate,
    db: Session = Depends(get_db),
    authorization: str = Header(...),
):
    await check_authorization(authorization=authorization, user_type="recruiter")
    if not jobcrud.vacancy.get(db, job_vacancy_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Job Vacancy not found"
        )
    data = job_vacancy.dict(exclude_unset=True)
    skills = data.pop("skill", [])
    skills_delete = data.pop("skills_delete", [])
    resp = jobcrud.vacancy.update(db, job_vacancy_id, data)
    if not resp:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Data not updated to Database",
        )
    for skill in skills_delete:
        if not jobcrud.skills.delete(db, skill):
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Data not deleted from Database",
            )
    for skill in skills:
        if not jobcrud.skills.create(
            db, jobschema.JobSkillsCreate(job_id=job_vacancy_id, skill=skill)
        ):
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Data not updated to Database",
            )
    return {"details": "Job Vacancy Updated successfully"}

@job_vacancy_router.delete("/user/{user_id}")
async def delete_job_vacancy_by_user_id(
    user_id: int, db: Session = Depends(get_db), authorization: str = Header(...)
):
    await check_authorization(authorization=authorization, user_type="recruiter")
    if not jobcrud.vacancy.delete_by_user_id(db, user_id):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Data not deleted from Database",
        )
    return {"details": "Job Vacancy Deleted successfully"}
# Delete job vacancy by ID
@job_vacancy_router.delete("/{job_vacancy_id}")
async def delete_job_vacancy(
    job_vacancy_id: int, db: Session = Depends(get_db), authorization: str = Header(...)
):
    await check_authorization(authorization=authorization, user_type="recruiter")
    # Retrieve the job vacancy to ensure it exists
    db_job_vacancy = jobcrud.vacancy.get(db, job_vacancy_id)
    if db_job_vacancy is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Job Vacancy not found"
        )

    # Delete associated skills
    if not jobcrud.skills.delete_by_vacancy_id(db, job_vacancy_id):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Data not deleted from Database",
        )

    if not jobcrud.invite.delete_by_vacancy_id(db, job_vacancy_id):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Data not deleted from Database",
        )

    if not jobcrud.request.delete_by_vacancy_id(db, job_vacancy_id):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Data not deleted from Database",
        )

    # Finally, delete the job vacancy
    if not jobcrud.vacancy.delete(db, job_vacancy_id):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Data not deleted from Database",
        )

    return {
        "details": "Job Vacancy and all associated skills and tags deleted successfully"
    }


# Get All data from job vacancy for model
