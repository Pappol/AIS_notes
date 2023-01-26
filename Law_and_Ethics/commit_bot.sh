info="Commit: $(date)"
os="$(uname -s)"

echo "commit-bot detects OS: $os"

echo "$info" >> out.txt
echo "$info"
echo

# Ship it
git add out.txt
git commit -m "$info"
git push origin main # or "master" on old setups

cd -