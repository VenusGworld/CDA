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


def filtroCpf(cpf):
    if len(cpf) < 11:
        cpf = "--"
    elif len(cpf) == 11:
        cpf = cpf[0:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:]

    return cpf