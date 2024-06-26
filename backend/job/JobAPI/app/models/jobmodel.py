from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base


class JobVacancy(Base):
    __tablename__ = "job_vacancy"

    job_id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, index=True)
    job_name = Column(String(256))
    job_desc = Column(String(1024))
    company_name = Column(String(256))
    requirement = Column(String(5120))
    salary = Column(String(64))
    experience = Column(String(128))
    job_position = Column(String(32))
    location = Column(String(128))
    emp_type = Column(String(128))
    last_date = Column(DateTime)
    closed = Column(Boolean, default=False)
    no_of_request = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class JobTags(Base):
    __tablename__ = "job_tags"

    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey("job_vacancy.job_id"), index=True)
    tags = Column(String(125))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class JobSkill(Base):
    __tablename__ = "job_skill"

    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey("job_vacancy.job_id"), index=True)
    skill = Column(String(125))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class JobRequest(Base):
    __tablename__ = "job_requests"

    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, ForeignKey("job_vacancy.job_id"), index=True)
    user_id = Column(Integer, index=True)
    status = Column(String(64))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
