from openai import AsyncOpenAI
from app.core.config import settings

client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

class LLMService:

    async def generate(self, prompt: str):
        response = await client.chat.completions.create(
            model=settings.MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )

        return response.choices[0].message.content
