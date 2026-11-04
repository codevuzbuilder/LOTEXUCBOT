from aiogram import Router

router = Router()

# Agar handlerlar boshqa alohida fayllarda (masalan, user.py, admin.py) bo'lsa, 
# ularni shu yerda routerga ulab ketishingiz mumkin:
# from . import user, admin
# router.include_router(user.router)
# router.include_router(admin.router)
