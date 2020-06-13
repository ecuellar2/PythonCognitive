# https://docs.microsoft.com/en-us/azure/bot-service/bot-builder-tutorial-add-qna?view=azure-bot-service-4.0&tabs=python
# https://www.qnamaker.ai/
# C:\Python\Python38-32\python -m pip install botbuilder-core
# C:\Python\Python38-32\python -m pip install asyncio
# C:\Python\Python38-32\python -m pip install aiohttp
# C:\Python\Python38-32\python -m pip install cookiecutter
# C:\Python\Python38-32\python -m pip install botbuilder-ai
# C:\Python\Python38-32\python -m pip install flask

from flask import Config
from botbuilder.ai.qna import QnAMaker, QnAMakerEndpoint
from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount

#route = "/qnamaker/knowledgebases/xxx/generateAnswer"
# See https://aka.ms/about-bot-activity-message to learn more about the message and other activity types.
 
class MyBot(ActivityHandler):
    def __init__(self):
        self.qna_maker = QnAMaker(QnAMakerEndpoint(knowledge_base_id="xx",endpoint_key="xx",host="https://xxx.azurewebsites.net/qnamaker"))

    async def on_members_added_activity(self, members_added: [ChannelAccount], turn_context: TurnContext):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome to QnA!")

    async def on_message_activity(self, turn_context: TurnContext):
    # The actual call to the QnA Maker service, using turn_context.activity.text
        response = await self.qna_maker.get_answers(turn_context)
        if response and len(response) > 0:
            await turn_context.send_activity(MessageFactory.text(response[0].answer))
        else:
            await turn_context.send_activity("No QnA Maker answers were found.")

# How do I manage my knowledgebase?
