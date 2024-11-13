def pytest_addoption(parser):
    group = parser.getgroup('sppr-amipm')

    group.addoption(
        '--browser', dest='browser', metavar='browser', default='chrome', help='Browser. Default option is chrome'
    )

    group.addoption(
        '--ui_url',
        help='A way to override the ui_url for your tests.',
        metavar='ui_url',
        default='',
    )

    group.addoption(
        '--ui_url_mm',
        help='ui_url for media monitoring',
        metavar='ui_url_mm',
        default='ms.mos.ru',
    )

    group.addoption(
        '--ui_url_eo',
        help='ui_url for electronic office',
        metavar='ui_url_eo',
        default='office.mos.ru/arm',
    )

    group.addoption(
        '--ui_url_ps_arm',
        help='ui_url for ARM press service',
        metavar='ui_url_ps_arm',
        default='psmm.mos.ru/arm',
    )

    parser.addoption(
        '--remote_ip',
        help='A way to set remote url of selenoid',
        dest='remote_ip',
        metavar='remote_ip',
        # default='internal:Xai6eedaeGhepeiwoh5M@cview-bal1p.passport.local',
        default='selenoid6.c-view.mos.ru',
    )

    parser.addoption(
        '--remote_port',
        help='A way to set remote port of selenoid',
        dest='remote_port',
        metavar='remote_port',
        default='80',
    )

    parser.addoption(
        '--remote_ui',
        help='A way to set remote url of selenoid ui',
        dest='remote_ui',
        metavar='remote_ui',
        # default='internal:Xai6eedaeGhepeiwoh5M@cview-bal1p.passport.local',
        default='selenoid6.c-view.mos.ru',
    )

    parser.addoption(
        '--wait',
        help='(int) Value waiting of condition in seconds',
        dest='wait',
        metavar='wait',
        type=int,
        default=30,
    )

    parser.addoption(
        '--enable-video',
        action='store',
        dest='enable_video',
        type=bool,
        default=False,
        help='Enable recording video option',
    )

    parser.addoption(
        '--user-mm',
        action='store',
        dest='username_mm',
        type=str,
        default='Fmonitor',
        help='Username media monitoring',
    )
    parser.addoption(
        '--password-mm',
        action='store',
        dest='password_mm',
        type=str,
        default='H4nFcx13@32!+0!!BNa',
        help='Password media monitoring',
    )

    parser.addoption(
        '--user-eo',
        action='store',
        dest='username_eo',
        type=str,
        default='Fmonitor',
        help='Username electronic office',
    )
    parser.addoption(
        '--password-eo',
        action='store',
        dest='password_eo',
        type=str,
        default='H4nFcx',
        help='Password electronic office',
    )

    parser.addoption(
        '--user-ps_arm',
        action='store',
        dest='username_ps_arm',
        type=str,
        default='Fmonitor',
        help='Username ARM press service',
    )
    parser.addoption(
        '--password-ps_arm',
        action='store',
        dest='password_ps_arm',
        type=str,
        default='H4nFcx13@32!+0',
        help='Password ARM press service',
    )
