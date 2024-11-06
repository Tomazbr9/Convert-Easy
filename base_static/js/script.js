// Script para alternar a seleção de ícones e ajustar a lista de formatos
const icons = document.querySelectorAll('.file-type-icon');
const formatSelect = document.getElementById('format');
const file = document.getElementById('file')

icons.forEach(icon => {
    icon.addEventListener('click', () => {
        // Limpa a seleção anterior
        icons.forEach(i => i.classList.remove('selected'))

        // Adiciona a classe 'selected' ao ícone clicado
        icon.classList.add('selected')

        // Limpa as opções de formato
        formatSelect.innerHTML = ''

        // Adiciona opções de acordo com o tipo de arquivo selecionado
        const filetype = icon.getAttribute('data-filetype')
        if (filetype === 'video') {
            file.accept = ".mp4, .avi, .mkv"
            formatSelect.innerHTML = `
                <option value="mp4">MP4</option>
                <option value="avi">AVI</option>
                <option value="mov">MOV</option>
            `
        } else if (filetype === 'audio') {
            file.accept = ".mp3, .wav, .flac"
            formatSelect.innerHTML = `
                <option value="mp3">MP3</option>
                <option value="wav">WAV</option>
                <option value="flac">FLAC</option>
            `
        } else if (filetype === 'pdf') {
            file.accept = ".pdf"
            formatSelect.innerHTML = `
                <option value="docx">DOCX</option>
                <option value="IMG">IMG</option>
                <option value="txt">TXT</option>
            `
        } else if (filetype === 'word') {
            file.accept = ".doc, .docx"
            formatSelect.innerHTML = `
                <option value="pdf">PDF</option>
                <option value="txt">TXT</option>
            `
        } else if (filetype === 'image') {
            file.accept = ".jpg, .png, .gif"
            formatSelect.innerHTML = `
                <option value="jpeg">JPEG</option>
                <option value="png">PNG</option>
                <option value="gif">GIF</option>
            `
        }
    })
})


function showLoading(event) {
    // Previne o envio imediato do formulario
    event.preventDefault()
    // obtem o botão e seus elementos de texto e spinner
    const btnConvert = document.getElementById("btn-convert")
    const btnText = document.getElementById("btn-text")
    const spinner = document.getElementById("spinner")
    const fileName = document.getElementById("fileName")
    
    // Esconde o texto e mostra o spinner
    btnText.style.display = 'none'
    spinner.style.display = 'inline-block'

    const formData = new FormData(document.getElementById('upload-form'))

    fetch('/upload', {
        method: 'POST',
        body: formData
    }).then(response => response.json).then(data => {
        const containerResult = document.getElementById('resultContainer')
        const containerImage = document.getElementById('containerConvert')
        containerResult.style.display = 'block' 
        
        fileExtension = data.fileName.split('.').pop().toLowerCase()
        fileName.textContent = data.fileName
        btnConvert.href = data.fileUrl

        containerImage.innerHTML = ''
        if (['png', 'jpeg', 'jpg'].includes(fileExtension)){
            const img = document.createElement('img')
            img.src = data.fileUrl
            img.alt = 'Prévia do arquivo'
            containerImage.appendChild(img)
        } else if (fileExtension === 'pdf'){
            containerImage.innerHTML = '<i class="bi bi-file-earmark-pdf"></i>'
        } else if (['mp4', 'avi', 'mov'].includes(fileExtension)) {
            containerImage.innerHTML = '<i class="bi bi-filetype-mp4"></i>'
        } else if (fileExtension === 'docx'){
            containerImage.innerHTML = '<i class="bi bi-filetype-docx"></i>'
        } else if (fileExtension === 'txt'){
            containerImage.innerHTML = '<i class="bi bi-filetype-txt"></i>'
        } else {
            containerImage.innerHTML = '<i class="bi bi-file-earmark"></i>'
        }
    })
    .catch(error => {
        console.error('erro no upload: ', error)
        spinner.style.display = 'none'
        btnConvert.style.display = 'block'

        alert('erro no upload, tente novamente.')
    })
}
