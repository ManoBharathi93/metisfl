import concurrent.futures
from pathlib import Path
from typing import Callable

import grpc

from ..proto import learner_pb2_grpc
from ..utils.fedenv import ServerParams
from .common import GRPC_MAX_MESSAGE_LENGTH, get_endpoint


def get_server(
    server_params: ServerParams,
    servicer: learner_pb2_grpc.LearnerServiceServicer,
    add_servicer_to_server_fn: Callable,
    max_workers: int = 1000,
    max_message_length: int = GRPC_MAX_MESSAGE_LENGTH,
) -> grpc.Server:
    """Creates a gRPC server using the given server parameters and servicer.

    Parameters
    ----------
    server_params : ServerParams
        The server configuration parameters.
    servicer: learner_pb2_grpc.LearnerServiceServicer
        The servicer for the gRPC server.
    add_servicer_to_server_fn: Callable
        The function to add the servicer to the server.
    max_workers : int, optional
        The maximum number of clients that can be handled concurrently, by default 1000
    max_message_length : int, optional
        The maximum message length, by default GRPC_MAX_MESSAGE_LENGTH

    Returns
    -------
    grpc.Server
        The gRPC server, not started.
    """
    server_hostname = server_params.hostname
    server_port = server_params.port

    endpoint = get_endpoint(server_hostname, server_port)

    options = [
        ("grpc.max_concurrent_streams", max_workers),
        ("grpc.max_send_message_length", max_message_length),
    ]

    server = grpc.server(
        concurrent.futures.ThreadPoolExecutor(max_workers=max_workers),
        options=options,
    )

    add_servicer_to_server_fn(servicer, server)

    if server_params.root_certificate is not None:
        root_certificate = Path(server_params.root_certificate).read_bytes()
        public_certificate = Path(
            server_params.public_certificate).read_bytes()
        private_key = Path(server_params.private_key).read_bytes()

        server_credentials = grpc.ssl_server_credentials(
            ((private_key, public_certificate),),
            root_certificates=root_certificate,
        )
        server.add_secure_port(endpoint, server_credentials)
    else:
        server.add_insecure_port(endpoint)

    return server
