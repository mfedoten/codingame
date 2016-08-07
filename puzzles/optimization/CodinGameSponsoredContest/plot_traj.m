inp_data   = importdata('M1L1.txt');
positions  = inp_data(2:end,:);
field_size = inp_data(1,:);
field_data = load('fieldM1L1.txt');
field = field_data.';

cc = get(0,'DefaultAxesColorOrder');
cc(5,:) = [0.7, 0.7, 0.7];

positions = positions';
positions = reshape(positions,2,5,[]);
positions = permute(positions,[2 1 3]);

figure;
ha1 = axes();
imagesc(0:field_size(1)-1,0:field_size(2)-1,field);
colormap(1-gray);
axis([0 field_size(1)-1 0 field_size(2)-1]);
ha2 = axes('Position',ha1.Position);
ha2.XTick = []; ha2.YTick = [];
ha2.Color = 'none';
axis([0 field_size(1)-1 0 field_size(2)-1]); axis ij;
hold on;

for j = 1:length(positions)
    cla;
    for k = 1:5
        scatter(positions(k,1,j),positions(k,2,j),30,cc(k,:),'filled');
    end
    pause(0.2);
end