from fastapi import APIRouter, Depends, HTTPException, status, Header
from typing import Type, List
from .. import (
    get_db,
    Session,
    jobschema,
    jobcrud,
    check_authorization,
    get_current_user,
)


job_request_router = APIRouter(prefix="/job_request")


@job_request_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_job_request(
    job_request: jobschema.JobRequest,
    authorization: str = Header(...),
    db: Session = Depends(get_db),
):
    data = await get_current_user(authorization=authorization)
    job_req = jobschema.JobRequestCreate(**job_request.dict(), user_id=data["user_id"])
    res = jobcrud.request.create(db, job_req)
    if not res:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Data not updated to Database",
        )
    return {"detail": "Job Request created successfully"}


@job_request_router.get("/user", response_model=List[jobschema.JobRequest])
async def read_job_requests_by_user_id(
    authorization: str = Header(...), db: Session = Depends(get_db)
):
    user = await get_current_user(authorization=authorization)
    user_id = user.get("user_id")
    return jobcrud.request.get_all(db, user_id)


# Read job request by ID
@job_request_router.get("/{job_request_id}", response_model=jobschema.JobRequest)
async def read_job_request(job_request_id: int, db: Session = Depends(get_db)):
    db_job_request = jobcrud.request.get(db, job_request_id)
    if db_job_request is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Job Request not found"
        )
    return db_job_request


# Update job request by ID
@job_request_router.put("/{job_request_id}")
async def update_job_request(
    job_request_id: int,
    job_request: jobschema.JobRequestCreate,
    db: Session = Depends(get_db),
    authorization: str = Header(...),
):
    await check_authorization(authorization=authorization)
    db_job_request = jobcrud.request.update(db, job_request_id, job_request)
    if db_job_request is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Job Request not found"
        )
    return {"message": "Job Request updated successfully"}


# Delete job request by ID
@job_request_router.delete("/{job_request_id}")
async def delete_job_request(
    job_request_id: int, db: Session = Depends(get_db), authorization: str = Header(...)
):
    await check_authorization(authorization=authorization)
    db_job_request = jobcrud.request.get(db, job_request_id)
    if db_job_request is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Job Request not found"
        )
    jobcrud.request.delete(db, job_request_id)
    return {"message": "Job Request deleted successfully"}


# Get job requests by user ID
