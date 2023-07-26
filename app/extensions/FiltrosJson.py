import dateutil.parser


def filtroData(date, fmt=None):
    date = dateutil.parser.parse(date)
    native = date.replace(tzinfo=None)
    format='%d/%m/%Y'
    return native.strftime(format)


def filtroDataHora(date, fmt=None):
    native = date.replace(tzinfo=None)
    format='%d/%m/%Y %H:%M'
    return native.strftime(format)


def filtroNome(nome):
    return nome[:15]