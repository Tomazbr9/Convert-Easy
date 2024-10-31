// Script para alternar a seleção de ícones e ajustar a lista de formatos
const icons = document.querySelectorAll('.file-type-icon');
const formatSelect = document.getElementById('format');
const file = document.getElementById('file')

icons.forEach(icon => {
    icon.addEventListener('click', () => {
        // Limpa a seleção anterior
        icons.forEach(i => i.classList.remove('selected'));

        // Adiciona a classe 'selected' ao ícone clicado
        icon.classList.add('selected');

        // Limpa as opções de formato
        formatSelect.innerHTML = '';

        // Adiciona opções de acordo com o tipo de arquivo selecionado
        const filetype = icon.getAttribute('data-filetype');
        if (filetype === 'video') {
            file.accept = ".mp4, .avi, .mkv"
            formatSelect.innerHTML = `
                <option value="mp4">MP4</option>
                <option value="avi">AVI</option>
                <option value="mov">MOV</option>
            `;
        } else if (filetype === 'audio') {
            file.accept = ".mp3, .wav, .flac"
            formatSelect.innerHTML = `
                <option value="mp3">MP3</option>
                <option value="wav">WAV</option>
                <option value="flac">FLAC</option>
            `;
        } else if (filetype === 'pdf') {
            file.accept = ".pdf"
            formatSelect.innerHTML = `
                <option value="docx">DOCX</option>
                <option value="IMG">IMG</option>
                <option value="txt">TXT</option>
            `;
        } else if (filetype === 'word') {
            file.accept = ".doc, .docx"
            formatSelect.innerHTML = `
                <option value="pdf">PDF</option>
                <option value="txt">TXT</option>
            `;
        } else if (filetype === 'image') {
            file.accept = ".jpg, .png, .gif"
            formatSelect.innerHTML = `
                <option value="jpeg">JPEG</option>
                <option value="png">PNG</option>
                <option value="gif">GIF</option>
            `;
        }
    });
});