$(document).ready(function() {

    var levelNumber = getLevelFromURL(window.location.pathname);
    if (levelNumber == 2) {
        const url = new URL(window.location.href);
        url.searchParams.set('code', 'emVsb1phaHRldm5vR2VzbG8');
        window.history.pushState({}, '', url);
    }
    else if (levelNumber == 4) {
        $("#submit-form").hide();
        $("#submit-code").val("KONEC");
        $("#click-me-button").on("click", function () {
            $("#submit-form").submit();
        });
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
                console.log(response);
                if (response.result === "correct") {
                    alert("Rešitev je pravilna!");

                    if (response.status) {
                        // Handle redirect
                        if (response.status === 302 && response.url) {
                            window.location.href = response.url;
                        }
                    }
                    else {
                        window.location.href = "/levels/" + (parseInt(levelNumber) + 1);
                    }
                    ž
                } else {
                    alert("Napačna rešitev.");
                }
            },
            error: function(xhr, status, error) {
                console.error("Error submitting code:", error);
            }
        });
    });

    $("#get-clue-button").on("click", function() {

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