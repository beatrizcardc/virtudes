// ==============================================================================
// 1. CONFIGURAÇÃO DOS DADOS (O CORAÇÃO DO SEU JOGO)
// ==============================================================================
// ATENÇÃO: Você DEVE alterar os nomes dos arquivos abaixo (ex: 'sua-imagem-01.jpg') 
// para os nomes EXATOS das imagens que você salvou na sua pasta 'virtudes'.
// Se sua imagem for PNG, mude a extensão para .png (ex: 'virtudes/minha-foto.png')
// Altere também as frases para as que você deseja.

const cardsData = [
    { id: 1,  img: 'virtudes/foto1.png', text: 'Fluir en el proceso.' },
    { id: 2,  img: 'virtudes/foto2.png', text: 'Fluir en la vida misma.' },
    { id: 3,  img: 'virtudes/foto3.png', text: 'Fluir hacia la conexión.' },
    { id: 4,  img: 'virtudes/foto4.png', text: 'Fluir en la renuncia integral.' },
    { id: 5,  img: 'virtudes/foto5.png', text: 'Fluir en la instrospección.' },
    { id: 6,  img: 'virtudes/foto6.png', text: 'Fluir en la atención.' },
    { id: 7,  img: 'virtudes/foto7.png', text: 'Fluir en Egoencia.' },
    { id: 8,  img: 'virtudes/foto8.png', text: 'Fluir en Presencia.' },
    { id: 9,  img: 'virtudes/foto9.png', text: 'Fluir en la unidad.' },
    { id: 10, img: 'virtudes/foto10.png', text: 'Fluir en Transcendencia.' },
    { id: 11, img: 'virtudes/foto11.png', text: 'Fluir con amor.' }
];
// ==============================================================================


// --- Variáveis de controle e Referências ao HTML ---
let cardsPlayedCount = 0;
const totalCards = cardsData.length;

// Pegando os elementos da tela pelo ID para podermos mexer neles
const gameBoard = document.getElementById('game-board');
const overlay = document.getElementById('overlay');
const activeCard = document.getElementById('active-card');
const activeImg = document.getElementById('active-img');
const activeText = document.getElementById('active-text');
const gameOverMessage = document.getElementById('game-over-message');


// --- 2. Inicialização do Jogo ---
// Esta função roda assim que a página termina de carregar
function initGame() {
    // Para cada item na nossa lista de dados acima, cria uma carta na tela
    cardsData.forEach(data => {
        createCardElement(data);
    });
}


// --- 3. Função que cria o visual de cada carta pequena no tabuleiro ---
function createCardElement(data) {
    // Cria o elemento principal da carta
    const cardSlot = document.createElement('div');
    cardSlot.classList.add('card-slot');
    
    // Monta a estrutura interna (frente com a imagem da pasta virtudes, verso vazio)
    cardSlot.innerHTML = `
        <div class="card-inner">
            <div class="card-front">
                <img src="${data.img}" alt="Carta ${data.id}">
            </div>
            <div class="card-back"></div> 
        </div>
    `;

    // Adiciona o "ouvinte" de clique: quando clicar nesta carta, chama a função de abrir
    cardSlot.addEventListener('click', () => openCard(cardSlot, data));
    
    // Coloca a carta pronta dentro do tabuleiro na tela
    gameBoard.appendChild(cardSlot);
}


// --- 4. Lógica de Abrir (Ampliar e Virar) a Carta ---
function openCard(clickedSlotElement, data) {
    // Se a carta já foi usada (está invisível), não faz nada se clicar nela de novo
    if (clickedSlotElement.classList.contains('used')) return;

    // A. Prepara a carta GRANDE (que está escondida) com os dados da carta clicada
    activeImg.src = data.img;     // Coloca a imagem certa
    activeText.textContent = data.text; // Coloca a frase certa
    
    // B. Mostra a camada escura de fundo (overlay) e inicia o efeito de zoom
    overlay.classList.add('active');

    // C. Espera um pouquinho (100ms) para dar tempo do zoom começar e então vira a carta para mostrar a frase
    setTimeout(() => {
        activeCard.classList.add('flipped');
    }, 100);

    // D. Marca a carta pequena do tabuleiro como "usada" (para ela sumir)
    clickedSlotElement.classList.add('used');
    
    // E. Aumenta o contador de cartas jogadas
    cardsPlayedCount++;
}


// --- 5. Lógica de Fechar a Carta Ampliada ---
// Adiciona o evento: quando clicar na carta grande, ela deve fechar
activeCard.addEventListener('click', closeCard);

function closeCard() {
    // A. Desvira a carta grande (volta a mostrar a imagem e esconde a frase)
    activeCard.classList.remove('flipped');

    // B. Espera a animação de desvirar terminar (600ms, conforme o CSS)
    setTimeout(() => {
            // Esconde o overlay e remove o zoom
            overlay.classList.remove('active');
            
            // Limpa os dados da carta grande para ficar pronta para a próxima
            setTimeout(() => {
                activeImg.src = "";
                activeText.textContent = "";
                // Verifica se foi a última carta
                checkGameOver();
            }, 300); // Espera o overlay sumir completamente
    }, 600);
}


// --- 6. Verificar Fim de Jogo ---
function checkGameOver() {
    // Se o número de cartas jogadas for igual ao total de cartas (11)
    if (cardsPlayedCount === totalCards) {
        gameBoard.style.display = 'none'; // Remove o grid da tela
        gameOverMessage.style.display = 'block'; // Mostra a mensagem de parabéns
    }
}

// Comando que inicia o jogo apenas quando todo o HTML estiver carregado no navegador
document.addEventListener('DOMContentLoaded', initGame);