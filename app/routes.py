from app.database import db
from app.models import Person_db
from app.schemas.User_forms.output import Get_user_info_form
from app.tg_bot import send_message, app


@app.post("/form")
async def form(p: Get_user_info_form):
     obj = Person_db(name=p.name, telegram=p.telegram, direction=p.direction)
     db.add(obj)  # добавляем в бд
     db.commit()  # сохраняем изменения
     db.refresh(obj)  # обновляем состояние объекта
     await send_message(chat_id='1060346898' , text=f'Имя {p.name}\ntg: {p.telegram}\ndirection: {p.direction}')