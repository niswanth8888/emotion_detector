function runEmotionAnalysis() {
    const textToAnalyze = document.getElementById("textToAnalyze").value;
    const xhr = new XMLHttpRequest();

    xhr.open("GET", `/emotionDetector?textToAnalyze=${encodeURIComponent(textToAnalyze)}`, true);

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementById("system_response").innerHTML = xhr.responseText;
        }
    };

    xhr.send();
}
