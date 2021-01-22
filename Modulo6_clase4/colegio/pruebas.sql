--
-- PostgreSQL database dump
--

-- Dumped from database version 13.1
-- Dumped by pg_dump version 13.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: app_alumno; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.app_alumno (
    id integer NOT NULL,
    nombre character varying(50) NOT NULL,
    apellido character varying(50) NOT NULL,
    "Transportista_id" integer,
    curso_id integer NOT NULL
);


ALTER TABLE public.app_alumno OWNER TO postgres;

--
-- Name: app_alumno_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.app_alumno_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_alumno_id_seq OWNER TO postgres;

--
-- Name: app_alumno_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.app_alumno_id_seq OWNED BY public.app_alumno.id;


--
-- Name: app_asignatura; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.app_asignatura (
    id integer NOT NULL,
    nombre character varying(50) NOT NULL,
    descripcion character varying(50) NOT NULL,
    departamento_id_id integer NOT NULL
);


ALTER TABLE public.app_asignatura OWNER TO postgres;

--
-- Name: app_asignatura_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.app_asignatura_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_asignatura_id_seq OWNER TO postgres;

--
-- Name: app_asignatura_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.app_asignatura_id_seq OWNED BY public.app_asignatura.id;


--
-- Name: app_curso; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.app_curso (
    id integer NOT NULL,
    nivel character varying(50) NOT NULL,
    cantidad_de_alumnos integer NOT NULL
);


ALTER TABLE public.app_curso OWNER TO postgres;

--
-- Name: app_curso_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.app_curso_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_curso_id_seq OWNER TO postgres;

--
-- Name: app_curso_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.app_curso_id_seq OWNED BY public.app_curso.id;


--
-- Name: app_curso_profesor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.app_curso_profesor (
    id integer NOT NULL,
    curso_id integer NOT NULL,
    profesor_id integer NOT NULL
);


ALTER TABLE public.app_curso_profesor OWNER TO postgres;

--
-- Name: app_curso_profesor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.app_curso_profesor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_curso_profesor_id_seq OWNER TO postgres;

--
-- Name: app_curso_profesor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.app_curso_profesor_id_seq OWNED BY public.app_curso_profesor.id;


--
-- Name: app_departamento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.app_departamento (
    id integer NOT NULL,
    nombre character varying(50) NOT NULL
);


ALTER TABLE public.app_departamento OWNER TO postgres;

--
-- Name: app_departamento_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.app_departamento_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_departamento_id_seq OWNER TO postgres;

--
-- Name: app_departamento_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.app_departamento_id_seq OWNED BY public.app_departamento.id;


--
-- Name: app_profesor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.app_profesor (
    id integer NOT NULL,
    nombre character varying(50) NOT NULL,
    apellido character varying(50) NOT NULL,
    escuela character varying(100) NOT NULL,
    fecha_de_contratacion date NOT NULL,
    sueldo integer NOT NULL
);


ALTER TABLE public.app_profesor OWNER TO postgres;

--
-- Name: app_profesor_asignatura; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.app_profesor_asignatura (
    id integer NOT NULL,
    profesor_id integer NOT NULL,
    asignatura_id integer NOT NULL
);


ALTER TABLE public.app_profesor_asignatura OWNER TO postgres;

--
-- Name: app_profesor_asignatura_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.app_profesor_asignatura_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_profesor_asignatura_id_seq OWNER TO postgres;

--
-- Name: app_profesor_asignatura_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.app_profesor_asignatura_id_seq OWNED BY public.app_profesor_asignatura.id;


--
-- Name: app_profesor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.app_profesor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_profesor_id_seq OWNER TO postgres;

--
-- Name: app_profesor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.app_profesor_id_seq OWNED BY public.app_profesor.id;


--
-- Name: app_transportista; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.app_transportista (
    id integer NOT NULL,
    nombre character varying(50) NOT NULL,
    apellido character varying(50) NOT NULL,
    fecha_de_contratacion date NOT NULL,
    sueldo integer NOT NULL
);


ALTER TABLE public.app_transportista OWNER TO postgres;

--
-- Name: app_transportista_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.app_transportista_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.app_transportista_id_seq OWNER TO postgres;

--
-- Name: app_transportista_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.app_transportista_id_seq OWNED BY public.app_transportista.id;


--
-- Name: asignatura; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.asignatura (
    id bigint NOT NULL,
    nombre character varying(50),
    descripcion character varying(50),
    departamento_id integer
);


ALTER TABLE public.asignatura OWNER TO postgres;

--
-- Name: asignatura_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.asignatura_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.asignatura_id_seq OWNER TO postgres;

--
-- Name: asignatura_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.asignatura_id_seq OWNED BY public.asignatura.id;


--
-- Name: departamento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.departamento (
    id bigint NOT NULL,
    nombre character varying(50)
);


ALTER TABLE public.departamento OWNER TO postgres;

--
-- Name: departamento_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.departamento_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.departamento_id_seq OWNER TO postgres;

--
-- Name: departamento_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.departamento_id_seq OWNED BY public.departamento.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: profesor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.profesor (
    id bigint NOT NULL,
    nombre character varying(50),
    apellido character varying(50),
    escuela character varying(100),
    fecha_de_contratacion date
);


ALTER TABLE public.profesor OWNER TO postgres;

--
-- Name: profesor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.profesor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.profesor_id_seq OWNER TO postgres;

--
-- Name: profesor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.profesor_id_seq OWNED BY public.profesor.id;


--
-- Name: app_alumno id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_alumno ALTER COLUMN id SET DEFAULT nextval('public.app_alumno_id_seq'::regclass);


--
-- Name: app_asignatura id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_asignatura ALTER COLUMN id SET DEFAULT nextval('public.app_asignatura_id_seq'::regclass);


--
-- Name: app_curso id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_curso ALTER COLUMN id SET DEFAULT nextval('public.app_curso_id_seq'::regclass);


--
-- Name: app_curso_profesor id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_curso_profesor ALTER COLUMN id SET DEFAULT nextval('public.app_curso_profesor_id_seq'::regclass);


--
-- Name: app_departamento id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_departamento ALTER COLUMN id SET DEFAULT nextval('public.app_departamento_id_seq'::regclass);


--
-- Name: app_profesor id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_profesor ALTER COLUMN id SET DEFAULT nextval('public.app_profesor_id_seq'::regclass);


--
-- Name: app_profesor_asignatura id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_profesor_asignatura ALTER COLUMN id SET DEFAULT nextval('public.app_profesor_asignatura_id_seq'::regclass);


--
-- Name: app_transportista id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_transportista ALTER COLUMN id SET DEFAULT nextval('public.app_transportista_id_seq'::regclass);


--
-- Name: asignatura id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.asignatura ALTER COLUMN id SET DEFAULT nextval('public.asignatura_id_seq'::regclass);


--
-- Name: departamento id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.departamento ALTER COLUMN id SET DEFAULT nextval('public.departamento_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: profesor id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.profesor ALTER COLUMN id SET DEFAULT nextval('public.profesor_id_seq'::regclass);


--
-- Data for Name: app_alumno; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.app_alumno (id, nombre, apellido, "Transportista_id", curso_id) FROM stdin;
1	Jesus	Contreras	2	1
\.


--
-- Data for Name: app_asignatura; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.app_asignatura (id, nombre, descripcion, departamento_id_id) FROM stdin;
1	Biologia	 seres vivos	1
\.


--
-- Data for Name: app_curso; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.app_curso (id, nivel, cantidad_de_alumnos) FROM stdin;
1	2° Medio A	20
\.


--
-- Data for Name: app_curso_profesor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.app_curso_profesor (id, curso_id, profesor_id) FROM stdin;
\.


--
-- Data for Name: app_departamento; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.app_departamento (id, nombre) FROM stdin;
1	Ciencias
\.


--
-- Data for Name: app_profesor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.app_profesor (id, nombre, apellido, escuela, fecha_de_contratacion, sueldo) FROM stdin;
1	Jonathan	Olave	AWAKE	2020-01-01	800000
\.


--
-- Data for Name: app_profesor_asignatura; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.app_profesor_asignatura (id, profesor_id, asignatura_id) FROM stdin;
\.


--
-- Data for Name: app_transportista; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.app_transportista (id, nombre, apellido, fecha_de_contratacion, sueldo) FROM stdin;
1	Boris	Aracena	2018-05-01	500000
2	Manuel	Cabezas	2020-06-01	400000
\.


--
-- Data for Name: asignatura; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.asignatura (id, nombre, descripcion, departamento_id) FROM stdin;
\.


--
-- Data for Name: departamento; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.departamento (id, nombre) FROM stdin;
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	app	0001_initial	2021-01-20 13:00:28.250342-03
2	app	0002_profesor	2021-01-20 13:10:21.627858-03
3	app	0003_auto_20210121_1221	2021-01-21 12:22:44.83162-03
\.


--
-- Data for Name: profesor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.profesor (id, nombre, apellido, escuela, fecha_de_contratacion) FROM stdin;
\.


--
-- Name: app_alumno_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.app_alumno_id_seq', 1, true);


--
-- Name: app_asignatura_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.app_asignatura_id_seq', 1, true);


--
-- Name: app_curso_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.app_curso_id_seq', 1, true);


--
-- Name: app_curso_profesor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.app_curso_profesor_id_seq', 1, false);


--
-- Name: app_departamento_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.app_departamento_id_seq', 1, true);


--
-- Name: app_profesor_asignatura_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.app_profesor_asignatura_id_seq', 1, false);


--
-- Name: app_profesor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.app_profesor_id_seq', 1, true);


--
-- Name: app_transportista_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.app_transportista_id_seq', 2, true);


--
-- Name: asignatura_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.asignatura_id_seq', 1, false);


--
-- Name: departamento_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.departamento_id_seq', 1, false);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 3, true);


--
-- Name: profesor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.profesor_id_seq', 1, false);


--
-- Name: app_alumno app_alumno_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_alumno
    ADD CONSTRAINT app_alumno_pkey PRIMARY KEY (id);


--
-- Name: app_asignatura app_asignatura_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_asignatura
    ADD CONSTRAINT app_asignatura_pkey PRIMARY KEY (id);


--
-- Name: app_curso app_curso_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_curso
    ADD CONSTRAINT app_curso_pkey PRIMARY KEY (id);


--
-- Name: app_curso_profesor app_curso_profesor_curso_id_profesor_id_c3a11015_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_curso_profesor
    ADD CONSTRAINT app_curso_profesor_curso_id_profesor_id_c3a11015_uniq UNIQUE (curso_id, profesor_id);


--
-- Name: app_curso_profesor app_curso_profesor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_curso_profesor
    ADD CONSTRAINT app_curso_profesor_pkey PRIMARY KEY (id);


--
-- Name: app_departamento app_departamento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_departamento
    ADD CONSTRAINT app_departamento_pkey PRIMARY KEY (id);


--
-- Name: app_profesor_asignatura app_profesor_asignatura_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_profesor_asignatura
    ADD CONSTRAINT app_profesor_asignatura_pkey PRIMARY KEY (id);


--
-- Name: app_profesor_asignatura app_profesor_asignatura_profesor_id_asignatura_id_962a9fd7_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_profesor_asignatura
    ADD CONSTRAINT app_profesor_asignatura_profesor_id_asignatura_id_962a9fd7_uniq UNIQUE (profesor_id, asignatura_id);


--
-- Name: app_profesor app_profesor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_profesor
    ADD CONSTRAINT app_profesor_pkey PRIMARY KEY (id);


--
-- Name: app_transportista app_transportista_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_transportista
    ADD CONSTRAINT app_transportista_pkey PRIMARY KEY (id);


--
-- Name: asignatura asignatura_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.asignatura
    ADD CONSTRAINT asignatura_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: departamento pk_departamento; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.departamento
    ADD CONSTRAINT pk_departamento PRIMARY KEY (id);


--
-- Name: profesor profesor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.profesor
    ADD CONSTRAINT profesor_pkey PRIMARY KEY (id);


--
-- Name: app_alumno_Transportista_id_39ddcab7; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX "app_alumno_Transportista_id_39ddcab7" ON public.app_alumno USING btree ("Transportista_id");


--
-- Name: app_alumno_curso_id_a5b2e940; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX app_alumno_curso_id_a5b2e940 ON public.app_alumno USING btree (curso_id);


--
-- Name: app_asignatura_departamento_id_id_4f9e4b93; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX app_asignatura_departamento_id_id_4f9e4b93 ON public.app_asignatura USING btree (departamento_id_id);


--
-- Name: app_curso_profesor_curso_id_92d63322; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX app_curso_profesor_curso_id_92d63322 ON public.app_curso_profesor USING btree (curso_id);


--
-- Name: app_curso_profesor_profesor_id_5f523f8a; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX app_curso_profesor_profesor_id_5f523f8a ON public.app_curso_profesor USING btree (profesor_id);


--
-- Name: app_profesor_asignatura_asignatura_id_a8a52a99; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX app_profesor_asignatura_asignatura_id_a8a52a99 ON public.app_profesor_asignatura USING btree (asignatura_id);


--
-- Name: app_profesor_asignatura_profesor_id_8527dc0f; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX app_profesor_asignatura_profesor_id_8527dc0f ON public.app_profesor_asignatura USING btree (profesor_id);


--
-- Name: app_alumno app_alumno_Transportista_id_39ddcab7_fk_app_transportista_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_alumno
    ADD CONSTRAINT "app_alumno_Transportista_id_39ddcab7_fk_app_transportista_id" FOREIGN KEY ("Transportista_id") REFERENCES public.app_transportista(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: app_alumno app_alumno_curso_id_a5b2e940_fk_app_curso_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_alumno
    ADD CONSTRAINT app_alumno_curso_id_a5b2e940_fk_app_curso_id FOREIGN KEY (curso_id) REFERENCES public.app_curso(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: app_asignatura app_asignatura_departamento_id_id_4f9e4b93_fk_app_depar; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_asignatura
    ADD CONSTRAINT app_asignatura_departamento_id_id_4f9e4b93_fk_app_depar FOREIGN KEY (departamento_id_id) REFERENCES public.app_departamento(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: app_curso_profesor app_curso_profesor_curso_id_92d63322_fk_app_curso_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_curso_profesor
    ADD CONSTRAINT app_curso_profesor_curso_id_92d63322_fk_app_curso_id FOREIGN KEY (curso_id) REFERENCES public.app_curso(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: app_curso_profesor app_curso_profesor_profesor_id_5f523f8a_fk_app_profesor_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_curso_profesor
    ADD CONSTRAINT app_curso_profesor_profesor_id_5f523f8a_fk_app_profesor_id FOREIGN KEY (profesor_id) REFERENCES public.app_profesor(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: app_profesor_asignatura app_profesor_asignat_asignatura_id_a8a52a99_fk_app_asign; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_profesor_asignatura
    ADD CONSTRAINT app_profesor_asignat_asignatura_id_a8a52a99_fk_app_asign FOREIGN KEY (asignatura_id) REFERENCES public.app_asignatura(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: app_profesor_asignatura app_profesor_asignatura_profesor_id_8527dc0f_fk_app_profesor_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.app_profesor_asignatura
    ADD CONSTRAINT app_profesor_asignatura_profesor_id_8527dc0f_fk_app_profesor_id FOREIGN KEY (profesor_id) REFERENCES public.app_profesor(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: asignatura fk_departamento; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.asignatura
    ADD CONSTRAINT fk_departamento FOREIGN KEY (departamento_id) REFERENCES public.departamento(id);


--
-- PostgreSQL database dump complete
--

