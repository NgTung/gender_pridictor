$(document).ready(function () {
  $(".hasclear").keyup(function () {
    var t = $(this);
    t.next('span').toggle(Boolean(t.val()));
  });
  $(".searchclear").toggle(Boolean($(".name").val()));
  $(".searchclear").click(function () {
    $(this).prev().val('').focus();
    $(this).hide();
  });
});