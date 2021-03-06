# info.py
"""
   _____                                 _   
  |_   _|                               | |  
    | | ___  ___ ___  ___ _ __ __ _  ___| |_ 
    | |/ _ \/ __/ __|/ _ \ '__/ _` |/ __| __|
    | |  __/\__ \__ \  __/ | | (_| | (__| |_ 
    \_/\___||___/___/\___|_|  \__,_|\___|\__|                                                                                   
 
  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU Lesser General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.
"""
class Info():
	CURRENT_PROTOCOL = 84

	LOGIN_PACKET = 0x01
	PLAY_STATUS_PACKET = 0x02
	SERVER_TO_CLIENT_HANDSHAKE_PACKET = 0x03
	CLIENT_TO_SERVER_HANDSHAKE_PACKET = 0x04
	DISCONNECT_PACKET = 0x05
	BATCH_PACKET = 0x06
	TEXT_PACKET = 0x07
	SET_TIME_PACKET = 0x08
	START_GAME_PACKET = 0x09
	ADD_PLAYER_PACKET = 0x0a
	ADD_ENTITY_PACKET = 0x0b
	REMOVE_ENTITY_PACKET = 0x0c
	ADD_ITEM_ENTITY_PACKET = 0x0d
	TAKE_ITEM_ENTITY_PACKET = 0x0e
	MOVE_ENTITY_PACKET = 0x0f
	MOVE_PLAYER_PACKET = 0x10
	RIDER_JUMP_PACKET = 0x11
	REMOVE_BLOCK_PACKET = 0x12
	UPDATE_BLOCK_PACKET = 0x13
	ADD_PAINTING_PACKET = 0x14
	EXPLODE_PACKET = 0x15
	LEVEL_EVENT_PACKET = 0x16
	BLOCK_EVENT_PACKET = 0x17
	ENTITY_EVENT_PACKET = 0x18
	MOB_EFFECT_PACKET = 0x19
	UPDATE_ATTRIBUTES_PACKET = 0x1a
	MOB_EQUIPMENT_PACKET = 0x1b
	MOB_ARMOR_EQUIPMENT_PACKET = 0x1c
	INTERACT_PACKET = 0x1e
	USE_ITEM_PACKET = 0x1f
	PLAYER_ACTION_PACKET = 0x20
	HURT_ARMOR_PACKET = 0x21
	SET_ENTITY_DATA_PACKET = 0x22
	SET_ENTITY_MOTION_PACKET = 0x23
	SET_ENTITY_LINK_PACKET = 0x24
	SET_HEALTH_PACKET = 0x25
	SET_SPAWN_POSITION_PACKET = 0x26
	ANIMATE_PACKET = 0x27
	RESPAWN_PACKET = 0x28
	DROP_ITEM_PACKET = 0x29
	CONTAINER_OPEN_PACKET = 0x2a
	CONTAINER_CLOSE_PACKET = 0x2b
	CONTAINER_SET_SLOT_PACKET = 0x2c
	CONTAINER_SET_DATA_PACKET = 0x2d
	CONTAINER_SET_CONTENT_PACKET = 0x2e
	CRAFTING_DATA_PACKET = 0x2f
	CRAFTING_EVENT_PACKET = 0x30
	ADVENTURE_SETTINGS_PACKET = 0x31
	BLOCK_ENTITY_DATA_PACKET = 0x32
	PLAYER_INPUT_PACKET = 0x33
	FULL_CHUNK_DATA_PACKET = 0x34
	SET_DIFFICULTY_PACKET = 0x35
	CHANGE_DIMENSION_PACKET = 0x36
	SET_PLAYER_GAMETYPE_PACKET = 0x37
	PLAYER_LIST_PACKET = 0x38
	TELEMETRY_EVENT_PACKET = 0x39
	SPAWN_EXPERIENCE_ORB_PACKET = 0x3a
	CLIENTBOUND_MAP_ITEM_DATA_PACKET = 0x3b
	MAP_INFO_REQUEST_PACKET = 0x3c
	REQUEST_CHUNK_RADIUS_PACKET = 0x3d
	CHUNK_RADIUS_UPDATED_PACKET = 0x3e
	ITEM_FRAME_DROP_ITEM_PACKET = 0x3f
	REPLACE_SELECTED_ITEM_PACKET = 0x40
	ADD_ITEM_PACKET = 0x41
