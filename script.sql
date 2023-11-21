create table accounts_user
(
    id           integer      not null,
    last_login   datetime,
    is_superuser bool         not null,
    first_name   varchar(150) not null,
    last_name    varchar(150) not null,
    is_staff     bool         not null,
    is_active    bool         not null,
    date_joined  datetime     not null,
    full_name    varchar(50)  not null,
    email        varchar(254) not null,
    password     varchar(100) not null,
    phone_number integer,
    avatar       varchar(100),
    is_verified  bool         not null,
    gender       bool,
    primary key (id autoincrement),
    unique (email),
    unique (phone_number)
);

create table account_emailaddress
(
    id        integer      not null,
    verified  bool         not null,
    "primary" bool         not null,
    user_id   bigint       not null,
    email     varchar(254) not null,
    primary key (id autoincrement),
    foreign key (user_id) references accounts_user
        deferrable initially deferred
);

create index account_emailaddress_upper
    on account_emailaddress ("(UPPER(""email""))");

create index account_emailaddress_user_id_2c513194
    on account_emailaddress (user_id);

create unique index account_emailaddress_user_id_email_987c8728_uniq
    on account_emailaddress (user_id, email);

create unique index unique_verified_email
    on account_emailaddress (email)
    where "verified";

create table account_emailconfirmation
(
    id               integer     not null,
    created          datetime    not null,
    sent             datetime,
    key              varchar(64) not null,
    email_address_id integer     not null,
    primary key (id autoincrement),
    unique (key),
    foreign key (email_address_id) references account_emailaddress
        deferrable initially deferred
);

create index account_emailconfirmation_email_address_id_5b7f8c58
    on account_emailconfirmation (email_address_id);

create table auth_group
(
    id   integer      not null,
    name varchar(150) not null,
    primary key (id autoincrement),
    unique (name)
);

create table accounts_user_groups
(
    id       integer not null,
    user_id  bigint  not null,
    group_id integer not null,
    primary key (id autoincrement),
    foreign key (user_id) references accounts_user
        deferrable initially deferred,
    foreign key (group_id) references auth_group
        deferrable initially deferred
);

create index accounts_user_groups_group_id_bd11a704
    on accounts_user_groups (group_id);

create index accounts_user_groups_user_id_52b62117
    on accounts_user_groups (user_id);

create unique index accounts_user_groups_user_id_group_id_59c0b32f_uniq
    on accounts_user_groups (user_id, group_id);

create table company_company
(
    id                  integer      not null,
    name                varchar(50)  not null,
    description         text         not null,
    address             varchar(100) not null,
    email               varchar(254) not null,
    phone_number        integer      not null,
    number_of_employees integer      not null,
    avatar              varchar(100) not null,
    social_link         varchar(254),
    industry            varchar(50)  not null,
    followers           integer      not null,
    created_date        datetime     not null,
    active              bool         not null,
    is_verified         bool         not null,
    primary key (id autoincrement),
    unique (name),
    unique (email),
    unique (phone_number)
);

create table cv_management_curriculumvitae
(
    id           integer      not null,
    name         varchar(50)  not null,
    image        varchar(100) not null,
    created_date datetime     not null,
    updated_date datetime     not null,
    active       bool         not null,
    user_id      bigint       not null,
    primary key (id autoincrement),
    foreign key (user_id) references accounts_user
        deferrable initially deferred
);

create index cv_management_curriculumvitae_user_id_216d1efb
    on cv_management_curriculumvitae (user_id);

create table django_content_type
(
    id        integer      not null,
    app_label varchar(100) not null,
    model     varchar(100) not null,
    primary key (id autoincrement)
);

create table auth_permission
(
    id              integer      not null,
    content_type_id integer      not null,
    codename        varchar(100) not null,
    name            varchar(255) not null,
    primary key (id autoincrement),
    foreign key (content_type_id) references django_content_type
        deferrable initially deferred
);

create table accounts_user_user_permissions
(
    id            integer not null,
    user_id       bigint  not null,
    permission_id integer not null,
    primary key (id autoincrement),
    foreign key (user_id) references accounts_user
        deferrable initially deferred,
    foreign key (permission_id) references auth_permission
        deferrable initially deferred
);

create index accounts_user_user_permissions_permission_id_113bb443
    on accounts_user_user_permissions (permission_id);

create index accounts_user_user_permissions_user_id_e4f0a161
    on accounts_user_user_permissions (user_id);

create unique index accounts_user_user_permissions_user_id_permission_id_2ab516c2_uniq
    on accounts_user_user_permissions (user_id, permission_id);

create table auth_group_permissions
(
    id            integer not null,
    group_id      integer not null,
    permission_id integer not null,
    primary key (id autoincrement),
    foreign key (group_id) references auth_group
        deferrable initially deferred,
    foreign key (permission_id) references auth_permission
        deferrable initially deferred
);

create index auth_group_permissions_group_id_b120cbf9
    on auth_group_permissions (group_id);

create unique index auth_group_permissions_group_id_permission_id_0cd325b0_uniq
    on auth_group_permissions (group_id, permission_id);

create index auth_group_permissions_permission_id_84c5c92e
    on auth_group_permissions (permission_id);

create index auth_permission_content_type_id_2f476e4b
    on auth_permission (content_type_id);

create unique index auth_permission_content_type_id_codename_01ab375a_uniq
    on auth_permission (content_type_id, codename);

create table django_admin_log
(
    id              integer           not null,
    object_id       text,
    object_repr     varchar(200)      not null,
    action_flag     smallint unsigned not null,
    change_message  text              not null,
    content_type_id integer,
    user_id         bigint            not null,
    action_time     datetime          not null,
    primary key (id autoincrement),
    foreign key (content_type_id) references django_content_type
        deferrable initially deferred,
    foreign key (user_id) references accounts_user
        deferrable initially deferred,
    check ("action_flag" >= 0)
);

create index django_admin_log_content_type_id_c4bce8eb
    on django_admin_log (content_type_id);

create index django_admin_log_user_id_c564eba6
    on django_admin_log (user_id);

create unique index django_content_type_app_label_model_76bd3d3b_uniq
    on django_content_type (app_label, model);

create table django_migrations
(
    id      integer      not null,
    app     varchar(255) not null,
    name    varchar(255) not null,
    applied datetime     not null,
    primary key (id autoincrement)
);

create table django_session
(
    session_key  varchar(40) not null,
    session_data text        not null,
    expire_date  datetime    not null,
    primary key (session_key)
);

create index django_session_expire_date_a5c62663
    on django_session (expire_date);

create table django_site
(
    id     integer      not null,
    name   varchar(50)  not null,
    domain varchar(100) not null,
    primary key (id autoincrement),
    unique (domain)
);

create table job_jobdescription
(
    id                 integer     not null,
    name               varchar(50) not null,
    wage_start         integer     not null,
    wage_end           integer     not null,
    location           varchar(50) not null,
    deadline           date        not null,
    description        text        not null,
    requirements       text        not null,
    benefits           text        not null,
    position           varchar(50) not null,
    experience_year    varchar(20) not null,
    number_of_recruits integer,
    work_form          varchar(20) not null,
    gender             varchar(20),
    created_date       datetime    not null,
    updated_date       datetime    not null,
    active             bool        not null,
    company_id         bigint      not null,
    primary key (id autoincrement),
    foreign key (company_id) references company_company
        deferrable initially deferred
);

create table job_jobapplication
(
    id               integer  not null,
    application_date datetime not null,
    active           bool     not null,
    job_id           bigint   not null,
    user_id          bigint   not null,
    primary key (id autoincrement),
    foreign key (job_id) references job_jobdescription
        deferrable initially deferred,
    foreign key (user_id) references accounts_user
        deferrable initially deferred
);

create index job_jobapplication_job_id_d0b0e713
    on job_jobapplication (job_id);

create index job_jobapplication_user_id_94d88484
    on job_jobapplication (user_id);

create index job_jobdescription_company_id_6396d9d7
    on job_jobdescription (company_id);

create table socialaccount_socialaccount
(
    id          integer      not null,
    provider    varchar(200) not null,
    uid         varchar(191) not null,
    last_login  datetime     not null,
    date_joined datetime     not null,
    user_id     bigint       not null,
    extra_data  text         not null,
    primary key (id autoincrement),
    foreign key (user_id) references accounts_user
        deferrable initially deferred,
    check ((JSON_VALID("extra_data") OR "extra_data" IS NULL))
);

create unique index socialaccount_socialaccount_provider_uid_fc810c6e_uniq
    on socialaccount_socialaccount (provider, uid);

create index socialaccount_socialaccount_user_id_8146e70c
    on socialaccount_socialaccount (user_id);

create table socialaccount_socialapp
(
    id          integer      not null,
    provider    varchar(30)  not null,
    name        varchar(40)  not null,
    client_id   varchar(191) not null,
    secret      varchar(191) not null,
    key         varchar(191) not null,
    provider_id varchar(200) not null,
    settings    text         not null,
    primary key (id autoincrement),
    check ((JSON_VALID("settings") OR "settings" IS NULL))
);

create table socialaccount_socialapp_sites
(
    id           integer not null,
    socialapp_id integer not null,
    site_id      integer not null,
    primary key (id autoincrement),
    foreign key (socialapp_id) references socialaccount_socialapp
        deferrable initially deferred,
    foreign key (site_id) references django_site
        deferrable initially deferred
);

create index socialaccount_socialapp_sites_site_id_2579dee5
    on socialaccount_socialapp_sites (site_id);

create index socialaccount_socialapp_sites_socialapp_id_97fb6e7d
    on socialaccount_socialapp_sites (socialapp_id);

create unique index socialaccount_socialapp_sites_socialapp_id_site_id_71a9a768_uniq
    on socialaccount_socialapp_sites (socialapp_id, site_id);

create table socialaccount_socialtoken
(
    id           integer not null,
    token        text    not null,
    token_secret text    not null,
    expires_at   datetime,
    account_id   integer not null,
    app_id       integer,
    primary key (id autoincrement),
    foreign key (account_id) references socialaccount_socialaccount
        deferrable initially deferred,
    foreign key (app_id) references socialaccount_socialapp
        deferrable initially deferred
);

create index socialaccount_socialtoken_account_id_951f210e
    on socialaccount_socialtoken (account_id);

create index socialaccount_socialtoken_app_id_636a42d7
    on socialaccount_socialtoken (app_id);

create unique index socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq
    on socialaccount_socialtoken (app_id, account_id);

create table sqlite_master
(
    type     TEXT,
    name     TEXT,
    tbl_name TEXT,
    rootpage INT,
    sql      TEXT
);

create table sqlite_sequence
(
    name,
    seq
);


