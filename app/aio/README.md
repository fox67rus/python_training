### Взаимодействие с API telegram
Кнопка Start в чате - отправляется запрос с командой и данными (request)

Updates - любые события содержащие сообщения для бота. До того, как сообщения попадут в 
*Updates* они попадают в *MidleWares* (можно использовать для логов или антифлуда)

Handlers - обработка событий. Назначение действий при поступлении той или иной команды.

Filters (Фильтры) - позволяют фильтровать обработку событий (разные реакции, разные пользователи).

FMS (машина состояний) - сообщить и запомнить состояние пользователю.

После обработки нужно сообщить пользователю, что команда обработана, для этого надо отправить команду на сервер Телеграм.

