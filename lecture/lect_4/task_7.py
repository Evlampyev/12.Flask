import asyncio


async def count():
    """Корутина"""
    print("Начало выполнения")
    await asyncio.sleep(1)
    print("Прошла 1 секунда")
    await asyncio.sleep(2)
    print("Прошло еще 2 секунды")
    return "Готово"


async def main():
    """Корутина"""
    result = await asyncio.gather(
                        count(), count(), count())  # Запускаются три задачи параллельно
    print(result)


asyncio.run(main())


