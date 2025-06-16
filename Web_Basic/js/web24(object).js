// let date_1 = new Date("2024");
// let date_2 = new Date("2024-02");
// let date_3 = new Date("2024-02-03");
// let date_4 = new Date("2024-02-03T18:00:00Z");

// console.log(date_4);

// let start = new Date('2025-05-01');
// let today = new Date();

// let pass_day = today.getTime()-start.getTime();
// pass_day = Math.round(pass_day/1000/60/60/24);

// console.log(pass_day);

// document.querySelector("#p_day").innerText = pass_day;

// let seed = prompt("전체 응모 수");
// let picked = Math.floor(Math.random() * seed) + 1;

// document.querySelector("#picked").innerText = picked;
// document.querySelector("#seed").innerText = seed;

// window.open("notice.html", "공지", "width=500, height=400, left=100, top=200");

const b_left = window.screenX;
const b_top = window.screenY;

const p_left = b_left + 100;
const p_top = b_top + 100;
window.open("notice.html", "공지", `width=500, height=400, left=${p_left}, top=${p_top}`);

function openPopup() {
    let newWin = window.open("notice.html", "공지", "width=500, height=400, left=100, top=200");
    if (newWin == null){
        alert("팝업이 차단되어 있습니다. 팝업을 허용해주세요.");
    }
}