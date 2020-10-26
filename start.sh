while true;
 do
  echo '请输入图片批处理操作模式（1 图片压缩，2图片缩放 3.添加水印 4 退出）'
  read NUM
  case $NUM in
  1)
    echo '请输入png格式压缩级别 1-5，建议选4 '
    read PNG_LEVEL
    echo '你选择的级别是'$PNG_LEVEL
    echo '请输入jpg格式压缩品质 1-100，建议选15 '
    read JPG_QUALITY
    echo '你选择的jpg格式压缩品质是'$JPG_QUALITY
    ./venv/bin/python3 ImageCompress.py $PNG_LEVEL $JPG_QUALITY
    echo '程序已退出'
    exit 1
    ;;
  2)
    echo '请输入resize模式和参数,
  如 1 960 540 表示图片压缩按像素来，生成图片像素为960*540，
  或 2 0.5 0.5 表示图片压缩按原图比例来，长宽缩放为原图的0.5 *0.5 '
    read MODEL WIDE HEIGHT
    echo "你选择的图片寛"$WIDE "高"$HEIGHT
    ./venv/bin/python3 ImageResize.py $MODEL $WIDE $HEIGHT
    echo '程序已退出'
    exit 1
    ;;
  3)
    echo '稍后 开发'
    ;;
  4)
    echo '程序已退出'
    exit 1
    ;;
  *)
    echo '请输入图片批处理操作模式（1 图片压缩，2图片缩放 3.添加水印 4 退出）'
    ;;
  esac
done
