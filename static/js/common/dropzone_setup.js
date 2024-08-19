$(document).ready(function(jQuery) {
    jQuery(function($) {
        if (window.location.href.indexOf("/change/") !== -1 || window.location.href.indexOf("/add/") !== -1) {
            var inlineGroups = ['projectimages'];

            inlineGroups.forEach(function(inlineGroup) {
                var groupSelector = `div#${inlineGroup}_set-group`;
                var headingSelector = `h2#${inlineGroup}_set-heading`;

                if ($(groupSelector).length) {
                    // Создаем контейнер для Dropzone под заголовком группы
                    $(headingSelector).after(`
                        <div id="${inlineGroup}_dropzone" class="dropzone" style="margin: 1rem 0;"></div>
                    `);

                    // Инициализация Dropzone
                    var myDropzone = new Dropzone(`#${inlineGroup}_dropzone`, {
                        url: "/", // Этот URL не используется, так как загрузка будет происходить локально
                        autoProcessQueue: false,
                        acceptedFiles: "image/png",
                        addRemoveLinks: true,
                        init: function() {
                            this.on("addedfile", function(file) {
                                // Автоматическое добавление новой формы
                                var addRowButton = document.querySelector(`${groupSelector} div.add-row a`);

                                addRowButton.click();

                                // Определение последнего добавленного инпута file
                                var formCount = $(`${groupSelector} .dynamic-${inlineGroup}_set`).length - 1;
                                var fileInput = $(`#id_${inlineGroup}_set-${formCount}-image`);

                                // Установка файла в инпут
                                var reader = new FileReader();
                                reader.onload = function(event) {
                                    // Создаем blob и устанавливаем в input
                                    var blob = dataURLtoBlob(event.target.result);
                                    var dataTransfer = new DataTransfer();
                                    dataTransfer.items.add(new File([blob], file.name));
                                    fileInput[0].files = dataTransfer.files;
                                };
                                reader.readAsDataURL(file);
                            });
                        }
                    });
                }
            });

            // Функция для конвертации DataURL в Blob
            function dataURLtoBlob(dataurl) {
                var arr = dataurl.split(','), mime = arr[0].match(/:(.*?);/)[1],
                    bstr = atob(arr[1]), n = bstr.length, u8arr = new Uint8Array(n);
                while(n--) {
                    u8arr[n] = bstr.charCodeAt(n);
                }
                return new Blob([u8arr], {type:mime});
            }

        }
    });
});