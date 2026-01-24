import asyncio

from digestify import Digestify, Topic


async def test_digestify() -> None:
    topic = Topic(
        name="World News",
        description=(
            "A summary of the most important global news stories covering politics, "
            "economics, conflicts, and major events from around the world."
        ),
    )

    digestify = Digestify()

    digest = await digestify.get_stories(topic)
    print(digest.model_dump_json(indent=4))


if __name__ == "__main__":
    asyncio.run(test_digestify())
