from argparse import ArgumentParser
from socket import socket, AF_INET, SOCK_STREAM
from common import __MSG_FIELD_SEP, __REQ_REG_USER, __REQ_GET_GAMES, \
    __REQ_CREATE_GAME, __REQ_ADD_PLAYER_TO_GAMEROOM, __REQ_MAKE_MOVE, \
    __REQ_INIT_GAME, __MSG_END, __RSP_OK, __REQ_CONNECT_SERVER_PORT

__USER_ID = None

def connect_server(server_port):
    server = ('127.0.0.1', server_port)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(server)
    sock.send("")
    return sock

def reg_user(sock, username):
    sock.send(__REQ_REG_USER + __MSG_FIELD_SEP + username)
    resp = sock.recv(1024)

    print(resp)
    header, resp = resp.split(__MSG_FIELD_SEP, 1)
    if header != __RSP_OK:
        print("miskit laks reg useris katki")
    else:
        print("Kasutaja id peaks olema", resp)
        __USER_ID = resp


# TODO: handle error reg user


def req_get_games(sock):
    sock.send(__REQ_GET_GAMES + __MSG_FIELD_SEP)
    resp = sock.recv(1024)
    header, resp = resp.split(__MSG_FIELD_SEP, 1)
    if header != __RSP_OK:
        print("miskit laks get games katki")
        #         TODO: handle error get games
    else:
        print "Response req_get_games:" + resp
        return resp

def req_create_game(sock, username):
    pass

