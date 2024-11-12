while read -r line; do
echo $line
mkdir -p $line
done < "myPWA\public\folders.txt"