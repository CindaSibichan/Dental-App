document.addEventListener("DOMContentLoaded", function() {
    function submitForm(event) {
        event.preventDefault();
        var startYear = document.getElementById('startYearSelect').value;
        var endYear = document.getElementById('endYearSelect').value;

        if (startYear && endYear) {
            var form = document.getElementById('year-range-form');
            form.submit();
        } else {
            alert('Please Select Both Start Year And End Year.');
        }
    }

    document.getElementById('dropdownButton').addEventListener('click', function(event) {
        event.stopPropagation();
        var dropdownMenu = document.getElementById('dropdownMenu');
        dropdownMenu.classList.toggle('hidden');
    });

    window.addEventListener('click', function(e) {
        var dropdownButton = document.getElementById('dropdownButton');
        var dropdownMenu = document.getElementById('dropdownMenu');
        if (!dropdownButton.contains(e.target) && !dropdownMenu.contains(e.target)) {
            dropdownMenu.classList.add('hidden');
        }
    });

    var startYearSelect = document.getElementById('startYearSelect');
    var currentYear = new Date().getFullYear();
    for (var year = 2020; year <= 2035; year++) {
        var option = document.createElement('option');
        option.text = option.value = year;
        startYearSelect.add(option);
    }

    var endYearSelect = document.getElementById('endYearSelect');
    for (var year = 2020; year <= 2035; year++) {
        var option = document.createElement('option');
        option.text = option.value = year;
        endYearSelect.add(option);
    }

    document.getElementById('year-range-form').addEventListener('submit', submitForm);

    document.getElementById('startYearSelect').addEventListener('change', function() {
        var startYear = document.getElementById('startYearSelect').value;
        var endYear = document.getElementById('endYearSelect').value;
        if (startYear && endYear) {
            submitForm();
        }
    });

    document.getElementById('endYearSelect').addEventListener('change', function() {
        var startYear = document.getElementById('startYearSelect').value;
        var endYear = document.getElementById('endYearSelect').value;
        if (startYear && endYear) {
            submitForm();
        }
    });
});
