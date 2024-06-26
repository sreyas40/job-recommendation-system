from .. import recruitermodel, recruiterschema, Session, SQLAlchemyError


def get_by_username(
    db: Session, username: str
) -> recruitermodel.RecruiterDetails | None:
    """
    Retrieve recruiter details by username.

    Args:
        db (Session): SQLAlchemy database session.
        username (str): Username of the recruiter.

    Returns:
        recruitermodel.RecruiterDetails or None: Recruiter details if found, else None.
    """
    try:
        return (
            db.query(recruitermodel.RecruiterDetails)
            .filter(recruitermodel.RecruiterDetails.username == username)
            .first()
        )
    except SQLAlchemyError:
        return


def get_by_emails(db: Session, email: str) -> recruitermodel.RecruiterDetails | None:
    """
    Retrieve recruiter details by email.

    Args:
        db (Session): SQLAlchemy database session.
        email (str): Email of the recruiter.

    Returns:
        recruitermodel.RecruiterDetails or None: Recruiter details if found, else None.
    """
    try:
        return (
            db.query(recruitermodel.RecruiterDetails)
            .filter(recruitermodel.RecruiterDetails.email == email)
            .first()
        )
    except SQLAlchemyError:
        return


def get(db: Session, user_id: int) -> recruitermodel.RecruiterDetails | None:
    """
    Retrieve recruiter details by user ID.

    Args:
        db (Session): SQLAlchemy database session.
        user_id (int): User ID of the recruiter.

    Returns:
        recruitermodel.RecruiterDetails or None: Recruiter details if found, else None.
    """
    try:
        return (
            db.query(recruitermodel.RecruiterDetails)
            .filter(recruitermodel.RecruiterDetails.user_id == user_id)
            .first()
        )
    except SQLAlchemyError:
        return


def create(db: Session, recruiter_details: recruiterschema.RecruiterDetails) -> bool:
    """
    Create a new recruiter details record in the database.

    Args:
        db (Session): SQLAlchemy database session.
        recruiter_details (recruiterschema.RecruiterDetails): Recruiter details to be created.

    Returns:
        bool : If successfull then return true else false
    """
    try:
        recruiter_details_model = recruitermodel.RecruiterDetails(
            **recruiter_details.dict()
        )
        db.add(recruiter_details_model)
        db.commit()
        return True
    except SQLAlchemyError:
        db.rollback()
        return False


def update_recruiter_details(
    db: Session, user_id: int, recruiter_details: recruiterschema.RecruiterDetails
) -> bool:
    """
    Update recruiter details in the database.

    Args:
        db (Session): SQLAlchemy database session.
        user_id (int): User ID of the recruiter.
        recruiter_details (recruiterschema.RecruiterDetails): Updated recruiter details.

    Returns:
        bool: if Updated successfully then True else false
    """
    try:
        db.query(recruitermodel.RecruiterDetails).filter(
            recruitermodel.RecruiterDetails.user_id == user_id
        ).update(recruiter_details.dict())
        db.commit()
        return True
    except SQLAlchemyError:
        db.rollback()
        return False


def delete_recruiter_details(db: Session, user_id: int) -> bool:
    """
    Delete recruiter details from the database.

    Args:
        db (Session): SQLAlchemy database session.
        user_id (int): User ID of the recruiter.

    Returns:
        bool: If Deleted Successfully true else false
    """
    try:
        db.query(recruitermodel.RecruiterDetails).filter(
            recruitermodel.RecruiterDetails.user_id == user_id
        ).delete()
        db.commit()
        return True
    except SQLAlchemyError:
        db.rollback()
        return False
