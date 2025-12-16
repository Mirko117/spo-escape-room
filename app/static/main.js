$(document).ready(function() {

    var levelNumber = getLevelFromURL(window.location.pathname);
    if (levelNumber == 2) {
        const url = new URL(window.location.href);
        url.searchParams.set('code', 'emVsb1phaHRldm5vR2VzbG8=');
        window.history.pushState({}, '', url);
    }

    $("#submit-form").submit(function(e) {
        e.preventDefault();
        
        var code = $("#submit-code").val();

        if (code === "") {
            return;
        }

        $.ajax({
            type: "POST",
            url: "/api/submit/" + levelNumber,
            contentType: "application/json",
            data: JSON.stringify({ code: code }),
            success: function(response) {
                if (response.result === "correct") {
                    alert("Correct code! Level completed.");
                    window.location.href = "/levels/" + (parseInt(levelNumber) + 1);
                } else {
                    alert("Incorrect code. Try again.");
                }
            },
            error: function(xhr, status, error) {
                console.error("Error submitting code:", error);
            }
        });
    });

    $("#get-clue-button").click(function() {

        $.ajax({
            type: "GET",
            url: "/api/clue/" + levelNumber,
            success: function(response) {
                $("#clue-text").text(response.clue);
            },
            error: function(xhr, status, error) {
                console.error("Error fetching clue:", error);
            }
        });
    });
});


function getLevelFromURL(url) {
    const urlParts = url.split('/');
    const level = urlParts[urlParts.indexOf('levels') + 1];
    return level;
}