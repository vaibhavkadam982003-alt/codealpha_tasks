const songs = [
  { title: "parvati boli shankar se", src: "C:\\Users\\prave\\Downloads\\Parvati Boli Shankar Se O Bholenath Ji - 320Kbps-(Mr-Jat.in).mp3" },
  { title: "khamoshiya", src: "C:\\Users\\prave\\Downloads\\Khamoshiyan Jeet Gannguli 320 Kbps.mp3" },
  { title: "Rama Rama Ratte Ratte", src: "C:\\Users\\prave\\Downloads\\Rama Rama Ratte Ratte 7.mp3" }
];

let index = 0;
const audio = document.getElementById("audio");
const title = document.getElementById("title");

function loadSong() {
  audio.src = songs[index].src;
  title.textContent = songs[index].title;
}

function playPause() {
  audio.paused ? audio.play() : audio.pause();
}

function nextSong() {
  index = (index + 1) % songs.length;
  loadSong();
  audio.play();
}

function prevSong() {
  index = (index - 1 + songs.length) % songs.length;
  loadSong();
  audio.play();
}

loadSong();
