from .Database import DB

def function_shell(app):
    
    @app.cli.command("create_db")
    def create_db():
        with app.app_context():
            DB.create_all()
            insereParametros()


    @app.cli.command("drop_db")
    def drop_db():
        with app.app_context():
            DB.drop_all()



def insereParametros():
    DB.session.execute("""
            INSERT INTO public.cda015
            (par_codigo, par_valor, par_desc)
            VALUES
                ('PAR_MANUT_CONTROL_CHAV', '12', 'Parâmetro para delimitar a data de consulta na tabela de manutenção de movimento de chaves'),
                ('PAR_MANUT_CONTROL_TERC', '12', 'Parâmetro para delimitar a data de consulta na tabela de manutenção de movimento de treceiros'),
                ('PAR_MANUT_CONTROL_GER', '12', 'Parâmetro para delimitar a data de consulta na tabela de manutenção de movimento de gerentes'),
                ('PAR_LOG_MANT_USER', '12', 'Parâmetro para delimitar a data de consulta nas tabelas de logs de usuários'),
                ('PAR_LOG_MANT_FUNC', '12', 'Parâmetro para delimitar a data de consulta nas tabelas de logs de funcionários'),
                ('PAR_LOG_MANT_CHAV', '12', 'Parâmetro para delimitar a data de consulta nas tabelas de logs de chaves'),
                ('PAR_LOG_MANT_TERC', '12', 'Parâmetro para delimitar a data de consulta nas tabelas de logs de terceiros'),
                ('PAR_LOG_MENSAGEM', '12', 'Parâmetro para delimitar a data de consulta nas tabelas de logs de mensagens');
            """)
    
    DB.session.commit()