cat > 0-body_size.sh <<'EOF'
#!/bin/bash
response=$(curl -s "$1")
echo -n "$response" | wc -c
EOF

chmod +x 0-body_size.sh

wc -l 0-body_size.sh

./0-body_size.sh 0.0.0.0:5000
