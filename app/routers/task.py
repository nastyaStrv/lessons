from fastapi import APIRouter

router = APIRouter(prefix='/task', tags=['task'])



# GET
@router.get('/')
async def all_tasks():
  pass

@router.get('/task_id')
async def task_by_id():
  pass


# POST
@router.post('/create')
async def create_task():
  pass


# PUT
@router.put('/update')
async def update_task():
  pass


# DELETE
@router.put('/delete')
async def delete_task():
  pass