from fastapi import HTTPException, status


class RaiseHttpException:
    @staticmethod
    def already_taken():
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Username already taken"
        )

    @staticmethod
    def user_not_found(username):
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User {username} not found",
        )

    @staticmethod
    def profile_not_found():
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found",
        )

    @staticmethod
    def unauthorized():
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )


    @staticmethod
    def inactive_user():
        return HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user",
        )

    @staticmethod
    def token_invalid():
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="token is invalid",
        )

    @staticmethod
    def invalid_token_type(
        token_type: str,
        TOKEN_TYPE: str,
    ):
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"invalid token type {token_type!r}, expected {TOKEN_TYPE!r}",
        )

    @staticmethod
    def country_not_found():
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Country not found",
        )

    @staticmethod
    def passwords_do_not_match():
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Passwords do not match",
        )

    @staticmethod
    def email_already_taken():
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already taken",
        )

    @staticmethod
    def must_agree_to_user_agreement():
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You must agree to user agreement",
        )
    
    @staticmethod
    def social_link_not_found():
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="social link not found",
        )

    @staticmethod
    def forbidden():
        return HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access is denied",
        )


ex = RaiseHttpException()
