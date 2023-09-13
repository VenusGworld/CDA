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
            (par_codigo, par_valor)
            VALUES
                ('PAR_MANUT_CONTROL_CHAV', '12'),
                ('PAR_MANUT_CONTROL_TERC', '12'),
                ('PAR_MANUT_CONTROL_GER', '12'),
                ('PAR_LOG_MANT_USER', '12'),
                ('PAR_LOG_MANT_FUNC', '12'),
                ('PAR_LOG_MANT_CHAV', '12'),
                ('PAR_LOG_MANT_TERC', '12');
            """)
    
    DB.session.commit()