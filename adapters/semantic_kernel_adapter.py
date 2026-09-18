import asyncio

from semantic_kernel import Kernel
from semantic_kernel.functions import kernel_function

from adapters.common import submit_to_authority


class AuthorityPlugin:
    @kernel_function(name="request_production_deployment")
    def request_production_deployment(self, request: dict) -> dict:
        return submit_to_authority(request)


async def invoke(request: dict) -> dict:
    kernel = Kernel()
    kernel.add_plugin(AuthorityPlugin(), plugin_name="IndependentAuthority")
    result = await kernel.invoke(
        plugin_name="IndependentAuthority",
        function_name="request_production_deployment",
        request=request,
    )
    return result.value


def run(request: dict) -> dict:
    return asyncio.run(invoke(request))
