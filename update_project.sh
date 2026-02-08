#!/bin/bash
cd ~/ai_fast_matching
echo "🔄 Обновление проекта на GitHub..."
git add .
git commit -m "Senior Update: synchronization of documentation and analysis scripts"
git push origin main
echo "✅ GitHub обновлен успешно!"
