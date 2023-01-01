import smpplib
from smpplib import consts


def _sim_send_sms(phone, text):
    client = None
    try:
        client = smpplib.client.Client(
            "213.230.120.114",
            "2778"
        )
        client.connect()
        try:
            client.bind_transmitter(
                system_id="road24",
                password="fcsuser24"
            )

            client.send_message(
                source_addr_ton=consts.SMPP_TON_INTL,
                # source_addr='Road24',
                dest_addr_ton=consts.SMPP_TON_INTL,
                destination_addr=phone,
                short_message=str.encode(text)
            )
        finally:
            if client.state in [smpplib.consts.SMPP_CLIENT_STATE_BOUND_TX]:
                try:
                    client.unbind()
                except smpplib.exceptions.UnknownCommandError as ex:
                    # https://github.com/podshumok/python-smpplib/issues/2
                    try:
                        client.unbind()
                    except smpplib.exceptions.PDUError as ex:
                        pass
    finally:
        if client:
            client.disconnect()


def sim_send_sms(phone, text):
    client = None
    try:
        client = smpplib.client.Client(
            "213.230.120.114",
            "2777"
        )
        client.connect()
        try:
            client.bind_transmitter(
                system_id="fcsuser",
                password="fcsuser"
            )

            client.send_message(
                source_addr_ton=consts.SMPP_TON_INTL,
                # source_addr='Road24',
                dest_addr_ton=consts.SMPP_TON_INTL,
                destination_addr=phone,
                short_message=str.encode(text)
            )
        finally:
            if client.state in [smpplib.consts.SMPP_CLIENT_STATE_BOUND_TX]:
                try:
                    client.unbind()
                except smpplib.exceptions.UnknownCommandError as ex:
                    # https://github.com/podshumok/python-smpplib/issues/2
                    try:
                        client.unbind()
                    except smpplib.exceptions.PDUError as ex:
                        pass
    finally:
        if client:
            client.disconnect()


_sim_send_sms("+998934748998", "test")
