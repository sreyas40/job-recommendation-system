from typing import List, Type

from .. import seekermodel, seekerschema, Session, SQLAlchemyError


def get_all(db: Session, user_id: int) -> List[Type[seekermodel.SeekersSkill]]:
    """
    Retrieve skills of a seeker.

    Args:
        db (Session): SQLAlchemy database.py session.
        user_id (int): User ID of the seeker.

    Returns:
        List[seekermodel.SeekersSkill]: Skills if found, else empty list.
    """
    try:
        return (
            db.query(seekermodel.SeekersSkill)
            .filter(seekermodel.SeekersSkill.user_id == user_id)
            .all()
        )
    except SQLAlchemyError:
        return []


def get(db: Session, skill_id: int) -> Type[seekermodel.SeekersSkill] | None:
    """
    Retrieve skills of a seeker.

    Args:
        db (Session): SQLAlchemy database.py session.
        skill_id (int): Skill Id to get from the DB.

    Returns:
        seekermodel.SeekersSkill: Skills if found, else None.
    """
    try:
        return (
            db.query(seekermodel.SeekersSkill)
            .filter(seekermodel.SeekersSkill.id == skill_id)
            .first()
        )
    except SQLAlchemyError:
        return None


def create(db: Session, skill: seekerschema.SeekersSkill) -> bool:
    """
    Create a new skill record for a seeker in the database.py.

    Args:
        db (Session): SQLAlchemy database.py session.
        skill (seekerschema.SeekersSkill): Skill details to be created.

    Returns:
        bool: True if creation is successful, False otherwise.
    """
    try:
        skill_model = seekermodel.SeekersSkill(**skill.dict())
        db.add(skill_model)
        db.commit()
        return True
    except SQLAlchemyError:
        db.rollback()
        return False


def get_all_list(db: Session, skills: List[str]) -> List[int]:
    """
    Retrieve the list of user IDs associated with the given skills from the database.py.

    Args:
        db (Session): The SQLAlchemy database.py session.
        skills (List[str]): A list of skills to filter the user IDs by.

    Returns:
        List[int]: A list of unique user IDs associated with the given skills. If an error occurs during the query, an empty list is returned.
    """
    try:
        result = (
            db.query(seekermodel.SeekersSkill.user_id)
            .filter(seekermodel.SeekersSkill.skill.in_(skills))
            .all()
        )
        return list(set([_[0] for _ in result]))
    except SQLAlchemyError:
        return []

def update(db: Session, id: int, updated_skill: seekerschema.SeekersSkill) -> bool:
    """
    Update skill details of a seeker in the database.py.

    Args:
        db (Session): SQLAlchemy database.py session.
        id (int): User ID of the seeker.
        updated_skill (seekerschema.SeekersSkill): Updated skill details.

    Returns:
        bool: True if update is successful, False otherwise.
    """
    try:
        update_data = {k: v for k, v in updated_skill.dict().items() if v is not None}

        db.query(seekermodel.SeekersSkill).filter(
            seekermodel.SeekersSkill.id == id
        ).update(update_data)
        db.commit()
        return True
    except SQLAlchemyError:
        db.rollback()
        return False


def delete(db: Session, id: int) -> bool:
    """
    Delete skill details of a seeker from the database.py.

    Args:
        db (Session): SQLAlchemy database.py session.
        id (int): User ID of the seeker.

    Returns:
        bool: True if deletion is successful, False otherwise.
    """
    try:
        db.query(seekermodel.SeekersSkill).filter(
            seekermodel.SeekersSkill.id == id
        ).delete()
        db.commit()
        return True
    except SQLAlchemyError:
        db.rollback()
        return False


def delete_by_user_id(db: Session, user_id: int) -> bool:
    """
    Delete skill details of a seeker from the database.py.

    Args:
        db (Session): SQLAlchemy database.py session.
        id (int): User ID of the seeker.

    Returns:
        bool: True if deletion is successful, False otherwise.
    """
    try:
        db.query(seekermodel.SeekersSkill).filter(
            seekermodel.SeekersSkill.user_id == user_id
        ).delete()
        db.commit()
        return True
    except SQLAlchemyError:
        db.rollback()
        return False
