const countdownEl = document.getElementById('countdown');
const startingMinutes = parseInt(document.getElementById('countdowntime').value) - 2;


let time = startingMinutes * 60;

// alert(countdownEl);

let timerInterval = setInterval(updateCountdown, 1000);

function updateCountdown() {
    let minutes = Math.floor(time / 60);
    let seconds = time % 60;

    minutes = minutes < 10 ? '0' + minutes : minutes;
    seconds = seconds < 10 ? '0' + seconds : seconds;

    countdownEl.innerHTML = `${minutes} : ${seconds}`;
    if (time > 0) {
        time--;
    }
}


const cards = document.querySelectorAll('.memory-card');

let hasFlippedCard = false;
let lockBoard = false;
let firstCard, secondCard;
let popalert = false;
let resault;
let cuplesAmount = parseInt(document.getElementById('countdowntime').value);

function flipCard() {
    if (lockBoard) return;
    if (this === firstCard) return;

    this.classList.add('flip');

    if (!hasFlippedCard) {
        hasFlippedCard = true;
        firstCard = this;
        resault = this;

        return;
    }

    secondCard = this;
    checkForMatch();
}

function checkForMatch() {
    let isMatch = firstCard.dataset.framework === secondCard.dataset.framework;
    isMatch ? disableCards() : unflipCards();
}

function disableCards() {
    firstCard.removeEventListener('click', flipCard);
    secondCard.removeEventListener('click', flipCard);
    popalert = true;

    resetBoard();
}

function unflipCards() {
    lockBoard = true;

    setTimeout(() => {
        firstCard.classList.remove('flip');
        secondCard.classList.remove('flip');

        resetBoard();
    }, 1500);
}

function resetBoard() {
    [hasFlippedCard, lockBoard] = [false, false];
    [firstCard, secondCard] = [null, null];
    setTimeout(() => {
        if (popalert) {
            popalert = false;
            cuplesAmount--;
            swal({
                title: resault.dataset.framework,
                text: "כל הכבוד, מצאת זוג",
                icon: "success",
                button: "יש",
            });
            if (cuplesAmount == 0) {
                clearInterval(timerInterval);
                setTimeout(() => {
                    document.getElementById('countdowntime').value = Math.max(time, 0);
                    // document.getElementById('countdowntime').type = 'submit';
                    document.getElementById('countdowntime').click();
                }, 2000)
            }
        }

    }, 800);
}

(function shuffle() {
    cards.forEach(card => {
        let randomPos = Math.floor(Math.random() * 12);
        card.style.order = randomPos;
    });
})();

cards.forEach(card => card.addEventListener('click', flipCard));