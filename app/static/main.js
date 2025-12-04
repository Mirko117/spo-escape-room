$(document).ready(function() {

    $("#submit-form").submit(function(e) {
        e.preventDefault();
        
        var code = $("#submit-code").val();

        if (code === "") {
            return;
        }

        var levelNumber = $("#level-number").text().trim();

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
        var levelNumber = $("#level-number").text().trim();

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