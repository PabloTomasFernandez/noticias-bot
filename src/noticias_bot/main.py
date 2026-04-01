from noticias_bot.adapters.news_client import NewsClient
from noticias_bot.adapters.ai_client import AIClient

def main() -> None:
    print("--- 🤖 NOTICIAS BOT: PROCESANDO CON IA ---")
    
    # Instanciamos los adaptadores
    news_api = NewsClient()
    ai_engine = AIClient()
    
    # 1. Traemos la 'data cruda' del adaptador de noticias
    data_cruda = news_api.obtener_noticia_destacada()
    print(f"DEBUG: Título recibido: {data_cruda.titulo}")
    
    # 2. Le pedimos a la IA que genere el objeto Noticia completo y validado
    print("🧠 La IA está trabajando...")
    noticia_final = ai_engine.resumir_noticia(
        titulo_original=data_cruda.titulo, 
        fuente=data_cruda.fuente
    )
    
    # 3. Resultado final con Pydantic
    print(f"\n📢 {noticia_final.titulo.upper()}")
    print(f"📝 Resumen: {noticia_final.resumen}")
    print(f"📰 Fuente: {noticia_final.fuente}")
    print(f"⏰ Procesado: {noticia_final.fecha_procesada.strftime('%H:%M:%S')}")
    print("\n--- 🤖 PROCESO FINALIZADO ---")

if __name__ == "__main__":
    main()