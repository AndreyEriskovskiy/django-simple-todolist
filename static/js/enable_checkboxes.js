document.addEventListener("DOMContentLoaded", function () {
    var selectAllCheckbox = document.getElementById("selectAll");
    var deleteAllButton = document.getElementById("delete_all");

    // Функция для обновления состояния кнопки "Очистить все"
    function updateDeleteAllButtonState() {
        var checkboxes = document.querySelectorAll('.form-check-input:not(#selectAll)');
        var allCheckboxesChecked = Array.from(checkboxes).every(function (checkbox) {
            return checkbox.checked;
        });

        deleteAllButton.disabled = !allCheckboxesChecked;
    }

    // Обработчик события изменения состояния чекбоксов
    function handleCheckboxChange() {
        updateDeleteAllButtonState();
    }

    // Добавление обработчика события для каждого чекбокса
    var checkboxes = document.querySelectorAll('.form-check-input:not(#selectAll)');
    checkboxes.forEach(function (checkbox) {
        checkbox.addEventListener('change', handleCheckboxChange);
    });

    // Обработчик события изменения состояния верхнего чекбокса
    selectAllCheckbox.addEventListener('change', function () {
        checkboxes.forEach(function (checkbox) {
            checkbox.checked = selectAllCheckbox.checked;
        });

        updateDeleteAllButtonState();
    });
});