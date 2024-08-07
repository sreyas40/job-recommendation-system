"""

Models for the UserAPI application.

Seekers Side.

"""
from sqlalchemy import (
    Column,
    String,
    Integer,
    Date,
    DateTime,
    ForeignKey,
    LargeBinary,
    Text,
)
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base


class SeekersDetails(Base):
    """
    Seekers details model.

    Represents the details of a seeker in the database.
    """
    __tablename__ = "seekers_details"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(32), unique=True)
    first_name = Column(String(32))
    last_name = Column(String(32))
    email = Column(String(32), unique=True)
    bio = Column(String(512))
    phone = Column(String(16))
    profile_banner_color = Column(String(10))
    address = Column(String(256))
    city = Column(String(128))
    country = Column(String(128))
    profile_picture = Column(Text(length=(2 ** 22) - 1))
    institution = Column(String(256))
    experience = Column(Integer, default=0)
    education = Column(String(256))
    contact_email = Column(String(32), default=email)
    dob = Column(Date)
    age = Column(Integer)
    gender = Column(String(16))
    location = Column(String(512))
    github = Column(String(32))
    website = Column(String(128))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class SeekersPOI(Base):
    """
    Seekers POI model.

    Represents the Points of Interest (POI) of a seeker in the database.
    """
    __tablename__ = "seekers_poi"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("seekers_details.user_id"))
    position = Column(String(32))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class SeekersEmpType(Base):
    """
    Seekers Employment Type model.

    Represents the type of employment a seeker in the database.
    """
    __tablename__ = "seekers_emp_type"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("seekers_details.user_id"), index=True)
    emp_type = Column(String(32))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class SeekersEducation(Base):
    """
    Seekers Education model.

    Represents the education details of a seeker in the database.
    """
    __tablename__ = "seekers_education"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("seekers_details.user_id"), index=True)
    education_title = Column(String(128))
    education_provider = Column(String(128))
    start_year = Column(String(4))
    end_year = Column(String(4))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class SeekersSkill(Base):
    """
    Seekers Skill model.

    Represents the skills of a seeker in the database.
    """
    __tablename__ = "seekers_skill"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("seekers_details.user_id"), index=True)
    skill = Column(String(32))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class SeekersFormerJob(Base):
    """
    Seekers Former Job model.

    Represents the previous job details of a seeker in the database.
    """
    __tablename__ = "seekers_former_job"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("seekers_details.user_id"), index=True)
    job_name = Column(String(32))
    company_name = Column(String(256))
    start_year = Column(String(32))
    end_year = Column(String(64))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class SeekersLocType(Base):
    """
    Seekers Loc Type model.

    Represents the type of location a seeker in the database.
    """
    __tablename__ = "seekers_loc_type"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("seekers_details.user_id"), index=True)
    loc_type = Column(String(32))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class SeekersCertificate(Base):
    """
    Seekers Certificate model.

    Represents the certificate details of a seeker in the database.
    """
    __tablename__ = "seekers_certificate"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("seekers_details.user_id"), index=True)
    certificate_name = Column(String(128))
    certificate_issuer = Column(String(128))
    credential_url = Column(String(256))
    issue_date = Column(String(32))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class SeekersLanguage(Base):
    """
    Seekers Language model.

    Represents the language details of a seeker in the database.
    """
    __tablename__ = "seekers_language"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("seekers_details.user_id"), index=True)
    language = Column(String(32))
    language_proficiency = Column(String(32))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)