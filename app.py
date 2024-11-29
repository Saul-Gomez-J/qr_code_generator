import streamlit as st
import qrcode
from PIL import Image
import io

def create_colored_qr(url, fill_color="#000000", back_color="#FFFFFF"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Crear el QR con los colores especificados
    qr_image = qr.make_image(fill_color=fill_color, back_color=back_color)
    return qr_image

def main():
    st.title("Generador de Códigos QR")
    st.write("Genera códigos QR personalizados a partir de URLs")

    # Campo para la URL
    url = st.text_input("Ingresa la URL:", "https://www.ejemplo.com")

    # Selectores de color
    col1, col2 = st.columns(2)
    with col1:
        qr_color = st.color_picker("Color del QR:", "#000000")
    with col2:
        background_color = st.color_picker("Color del fondo:", "#FFFFFF")

    if st.button("Generar QR"):
        if url:
            # Generar el código QR
            qr_image = create_colored_qr(url, qr_color, background_color)
            
            # Convertir la imagen para mostrarla
            img_buffer = io.BytesIO()
            qr_image.save(img_buffer, format="PNG")
            
            # Mostrar la imagen
            st.image(img_buffer.getvalue(), caption="Tu código QR")
            
            # Botón de descarga
            st.download_button(
                label="Descargar QR",
                data=img_buffer.getvalue(),
                file_name="qr_code.png",
                mime="image/png"
            )
        else:
            st.error("Por favor, ingresa una URL válida")

if __name__ == "__main__":
    main()