/* FFCallerDB作成 */
/*
sqlite3 ./ffc_db.sqlite3 < ./create_ffc_db.sql
*/

/* Target */
create table Target (
	target_id integer,
	file_id integer,
	item_order integer,
	primary key (
		target_id
	)
);

/* Trim */
create table Trim (
	target_id integer,
	start_time real,
	end_time real,
	start_frame integer,
	end_frame integer,
	frame_input_flag boolean,
	video_fade_in real,
	video_fade_out real,
	audio_fade_in real,
	audio_fade_out real,
	is_fade_from_white boolean,
	is_fade_to_white boolean,
	primary key (
		target_id
	)
);

/* File */
create table File (
	file_id integer,
	filename text,
	filepath text,
	workpath text,
	webpath text,
	primary key (
		file_id
	)
);

/* Format */
create table Format (
	file_id integer,
	nb_streams integer,
	duration real,
	size integer,
	primary key (
		file_id
	)
);

/* Stream */
create table Stream (
	file_id integer,
	stream_index integer,
	codec_type text,
	codec_name text,
	codec_long_name text,
	duration real,
	bit_rate integer,
	primary key (
		file_id,
		stream_index
	)
);

/* Video */
create table Video (
	file_id integer,
	stream_index integer,
	width integer,
	height integer,
	r_frame_rate text,
	nb_frames integer,
	primary key (
		file_id,
		stream_index
	)
);

/* Audio */
create table Audio (
	file_id integer,
	stream_index integer,
	sample_rate integer,
	primary key (
		file_id,
		stream_index
	)
);

/* 終了 */
.exit
