const titleInput = document.querySelector("#title-input");
const hiddenBodyInput = document.querySelector("#hidden-body");
const editor = toastui.Editor.factory({
  el: document.querySelector("#editor"),
  height: "400px", // 에디터의 높이를 설정합니다.
  initialEditType: "markdown",
  previewStyle: "vertical",
});

document.querySelector("#editor-form").addEventListener("submit", (event) => {
  // 기본 폼 제출을 막습니다.
  event.preventDefault();

  // 에디터의 내용을 editor.getMarkdown()으로 가져옵니다.
  const title = titleInput.value;
  const body = editor.getMarkdown();

  // 숨겨진 입력 필드와 title 입력 필드의 값을 에디터의 내용과 title로 설정합니다.
  hiddenBodyInput.value = body;
  titleInput.value = title;

  // 폼을 제출합니다.
  event.target.submit();
});
