from sqlalchemy import (
    Column,
    String,
    Integer,
    DateTime,
    Boolean,
    ForeignKey,
    LargeBinary,
)
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base


class JobVacancy(Base):
    """
    Job vacancy model

    Represents a job vacancy in the database.
    """

    __tablename__ = "job_vacancy"

    job_id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, index=True)
    job_name = Column(String(256))
    job_desc = Column(String(1024))
    company_name = Column(String(256))
    company_pic = Column(LargeBinary(length=(2 ** 24) - 1))
    company_username = Column(String(128))
    requirement = Column(String(5120))
    salary = Column(String(256))
    experience = Column(String(128))
    work_style = Column(String(64))
    job_position = Column(String(32))
    location = Column(String(128))
    working_days = Column(String(128))
    emp_type = Column(String(128))
    last_date = Column(DateTime)
    closed = Column(Boolean, default=False)
    no_of_request = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class JobSkill(Base):
    """
    Job skill model

    Represents the skills required for a job in the database.
    """

    __tablename__ = "job_skill"

    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey("job_vacancy.job_id"), index=True)
    skill = Column(String(125))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class JobRequest(Base):
    """
    Job request model

    Represents the job requests made by users for a particular job in the database.
    """

    __tablename__ = "job_requests"

    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey("job_vacancy.job_id"), index=True)
    user_id = Column(Integer, index=True)
    status = Column(String(64))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
class JobInvite(Base):
    """
    Job invite model

    Represents the invitations sent to users for a particular job in the database.
    """

    __tablename__ = "job_invite"

    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey("job_vacancy.job_id"), index=True)
    company_id = Column(Integer, index=True)
    status = Column(String(64))
    user_id = Column(Integer, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)