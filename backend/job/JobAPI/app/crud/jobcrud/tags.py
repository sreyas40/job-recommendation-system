from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import List, Type

from .. import jobschema, jobmodel


def get_all(db: Session, job_id: int) -> List[Type[jobschema.JobTags]]:
    """
    Retrieve job tags associated with a user ID from the database.

    Args:
        db (Session): SQLAlchemy database session.
        job_id (int): ID of the job whose job tags are to be retrieved.

    Returns:
        List[jobschema.JobTags]: List of job tags objects associated with the user.
    """
    try:
        return (
            db.query(jobmodel.JobTags).filter(jobmodel.JobTags.job_id == job_id).all()
        )
    except SQLAlchemyError:
        return []


def get(db: Session, job_tags_id: int) -> Type[jobmodel.JobTags] | None:
    """
    Retrieve a job tags from the database by ID.

    Args:
        db (Session): SQLAlchemy database session.
        job_tags_id (int): ID of the job tags to retrieve.

    Returns:
        jobmodel.JobTags: Job tags object if found, None otherwise.
    """
    try:
        return (
            db.query(jobmodel.JobTags)
            .filter(jobmodel.JobTags.id == job_tags_id)
            .first()
        )
    except SQLAlchemyError:
        return None


def create(db: Session, job_tags: jobschema.JobTagsCreate) -> bool:
    """
    Create a new job tags in the database.

    Args:
        db (Session): SQLAlchemy database session.
        job_tags (jobschema.JobTagsCreate): Details of the job tags to create.

    Returns:
        jobmodel.JobTags: Created job tags object.
    """
    try:
        db_job_tags = jobmodel.JobTags(**job_tags.dict())
        db.add(db_job_tags)
        db.commit()
        return True
    except SQLAlchemyError:
        db.rollback()
        return False


# Update


def update(db: Session, job_tags_id: int, job_tags: jobschema.JobTagsCreate):
    """
    Update a job tags in the database.

    Args:
        db (Session): SQLAlchemy database session.
        job_tags_id (int): ID of the job tags to update.
        job_tags (jobschema.JobTagsCreate): Updated job tags details.

    Returns:
        jobmodel.JobTags: Updated job tags object.
    """
    try:

        db.query(jobmodel.JobTags).filter(
            jobmodel.JobTags.id == job_tags_id
        ).first().update(job_tags.dict())
        db.commit()
        return True

    except SQLAlchemyError:
        db.rollback()
        return False


def delete(db: Session, job_tags_id: int):
    """
    Delete a job tags from the database.

    Args:
        db (Session): SQLAlchemy database session.
        job_tags_id (int): ID of the job tags to delete.

    Returns:
        None
    """
    try:
        db.query(jobmodel.JobTags).filter(jobmodel.JobTags.id == job_tags_id).delete()
        db.commit()
        return True
    except SQLAlchemyError:
        db.rollback()
        return False
