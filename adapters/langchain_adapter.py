from langchain_core.runnables import RunnableLambda

from adapters.common import submit_to_authority


def run(request: dict) -> dict:
    chain = RunnableLambda(submit_to_authority)
    return chain.invoke(request)

