from fastapi import APIRouter

router = APIRouter(prefix='/user', tags=['user'])



# GET
@router.get('/')
async def all_users():
  pass

@router.get('/user_id')
async def user_by_id():
  pass


# POST
@router.post('/create')
async def create_user():
  pass


# PUT
@router.put('/update')
async def update_user():
  pass


# DELETE
@router.put('/delete')
async def delete_user():
  pass